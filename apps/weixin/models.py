# coding=utf-8
import datetime
import time
import logging

from dateutil.relativedelta import relativedelta
from django.conf import settings

from . import conf as wx_conf
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.http import urlquote, urlunquote
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from wechat_sdk import WechatConf, WechatBasic
from wechat_sdk.exceptions import OfficialAPIError
from weixin.login import WeixinLogin
from weixin.base import Map
from weixin.mp import WeixinMP
from weixin.pay import WeixinPay, WeixinError, WeixinPayError
from core.auth_user.models import UserProfileMixin

log = logging.getLogger(__name__)


class WxApp(models.Model):
    name = wx_conf.APP_NAME
    app_id = wx_conf.APP_ID
    app_secret = wx_conf.APP_SECRET
    mch_id = wx_conf.MCH_ID
    mch_key = wx_conf.MCH_KEY

    @property
    def is_token_expired(self):
        # expired return true
        if not isinstance(self.token_expiry, datetime.datetime):
            return True
        return self.token_expiry - timezone.now() < datetime.timedelta(seconds=60)

    @property
    def is_ticket_expired(self):
        if not isinstance(self.ticket_expiry, datetime.datetime):
            return True
        return self.ticket_expiry - timezone.now() < datetime.timedelta(seconds=60)

    def get_access_token(self):
        if self.is_token_expired:
            try:
                conf = WechatConf(appid=self.app_id, appsecret=self.app_secret)
                access_token_dict = conf.get_access_token()
                self.access_token = access_token_dict['access_token']
                self.token_expiry = self.from_timestamp(access_token_dict['access_token_expires_at'])
                self.save(update_fields=['access_token', 'token_expiry'])
                log.info('Update token = %s, %s' % (self.access_token, self.token_expiry))
            except OfficialAPIError as e:
                log.error('[get_access_token] code=%s, %s' % (e.errcode, e.errmsg))

        return self.access_token

    def get_jsapi_ticket(self):
        if self.is_ticket_expired:
            try:
                conf = WechatConf(appid=self.app_id, appsecret=self.app_secret)
                jsapi_ticket_dict = conf.get_jsapi_ticket()
                self.jsapi_ticket = jsapi_ticket_dict['jsapi_ticket']
                self.ticket_expiry = self.from_timestamp(jsapi_ticket_dict['jsapi_ticket_expires_at'])
                self.save(update_fields=['jsapi_ticket', 'ticket_expiry'])
                log.info('Update jsapi_ticket = %s, %s' % (self.jsapi_ticket, self.ticket_expiry))
            except OfficialAPIError as e:
                log.error('[get_jsapi_ticket] code=%s, %s' % (e.errcode, e.errmsg))

        return self.jsapi_ticket

    def to_timestamp(self, dt):
        return time.mktime(dt.timetuple())

    def from_timestamp(self, ts):
        return datetime.datetime.fromtimestamp(ts, timezone.utc)

    @property
    def conf(self):
        conf_dict = {
            'appid': self.app_id,
            'appsecret': self.app_secret,
            'access_token': self.get_access_token(),
            'access_token_expires_at': self.to_timestamp(self.token_expiry),
            'jsapi_ticket': self.get_jsapi_ticket,
            'jsapi_ticket_expires_at': self.to_timestamp(self.ticket_expiry)
        }

        return WechatConf(**conf_dict)

    @property
    def api(self):
        return WechatBasic(conf=self.conf)

    @property
    def mp(self):
        return WeixinMP(self.app_id, self.app_secret,
                        '/tmp/.%s_access_token' % self.name,
                        '/tmp/.%s_jsapi_ticket' % self.name)

    @property
    def pay(self):
        url = reverse('weixin:pay_notify', args=[self.name])
        full_url = '%s%s' % (settings.BASE_URL, url)
        pay = WeixinPay(self.app_id, self.mch_id, self.mch_key, full_url)
        return pay

    @classmethod
    def get_login_url(self, scope=wx_conf.SCOPE_USERINFO, state=''):
        url = reverse('weixin:auth', args=[self.name])
        full_url = '%s%s' % (settings.BASE_URL, url)
        wx_login = WeixinLogin(self.app_id, self.app_secret)
        return wx_login.authorize(full_url, scope, state)


class WxReturnCode(object):
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'

    CHOICES = (
        (FAIL, FAIL),
        (SUCCESS, SUCCESS),
    )


class PaymentStatus(object):
    SUCCESS = 'SUCCESS'
    REFUND = 'REFUND'
    NOTPAY = 'NOTPAY'
    CLOSED = 'CLOSED'
    REVOKED = 'REVOKED'
    USERPAYING = 'USERPAYING'  # 用户支付中
    PAYERROR = 'PAYERROR'  # 支付失败

    CHOICES = (
        (SUCCESS, '支付成功'),
        (REFUND, '已退款'),
        (NOTPAY, '未付款'),
        (CLOSED, '支付关闭'),
        (REVOKED, '已撤销'),
        (USERPAYING, '支付中'),
        (PAYERROR, '支付失败'),
    )


class WxPayment(models.Model):
    # https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=9_2
    transaction_id = models.CharField(max_length=32, blank=True, null=True)  # 微信支付订单号
    return_code = models.CharField(max_length=16, blank=True,
                                   choices=WxReturnCode.CHOICES)  # 返回状态码 SUCCESS/FAIL
    return_msg = models.CharField(max_length=128, blank=True, null=True)  # 返回信息，如非空，为错误原因
    result_code = models.CharField(max_length=16, blank=True,
                                   choices=WxReturnCode.CHOICES)  # 业务结果	 SUCCESS/FAIL
    appid = models.CharField(max_length=32, blank=True, null=True)  # 公众账号ID
    mch_id = models.CharField(max_length=32, blank=True, null=True)  # 商户号
    device_info = models.CharField(max_length=32, blank=True, null=True)  # 设备号
    nonce_str = models.CharField(max_length=32, blank=True, null=True)  # 返回的随机字符串
    # 微信返回的签名值 https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=4_3
    sign = models.CharField(max_length=32, blank=True, null=True)
    sign_type = models.CharField(max_length=32, blank=True, default='MD5')
    err_code = models.CharField(max_length=32, blank=True, null=True)  # 错误代码
    err_code_des = models.CharField(max_length=128, blank=True, null=True)  # 错误信息描述
    openid = models.CharField(max_length=128, blank=True, null=True)
    is_subscribe = models.BooleanField(blank=False, null=False, default=False)  # 用户是否关注公众账号
    trade_type = models.CharField(max_length=16, blank=True, null=True)  # 交易类型
    bank_type = models.CharField(max_length=16, blank=True, null=True)
    total_fee = models.PositiveIntegerField(blank=True, null=True)  # 订单总金额，单位为分
    fee_type = models.CharField(max_length=8, blank=True, null=True)  # 货币种类
    out_trade_no = models.CharField(max_length=32, blank=True, null=True)  # 商户系统的订单号，与请求一致
    attach = models.CharField(max_length=128, blank=True, null=True)  # 商家数据包，原样返回
    # 支付完成时间，格式为yyyyMMddHHmmss，如2009年12月25日9点10分10秒表示为20091225091010
    time_end = models.CharField(max_length=16, blank=True, null=True)

    # 查询订单解口 orderquery返回
    trade_state = models.CharField(max_length=32, blank=True, choices=PaymentStatus.CHOICES)  # 交易状态
    # 交易状态描述,对当前查询订单状态的描述和下一步操作的指引
    trade_state_desc = models.CharField(max_length=256, blank=True, null=True)
    xml_response = models.TextField(blank=True, null=True)  # 原始xml信息

    @property
    def is_success(self):
        if self.return_code.upper() == WxReturnCode.SUCCESS == self.result_code.upper():
            return True
        else:
            return False

    def get_raw_response(self):
        return Map(WeixinPay(None, None, None, None).to_dict(self.xml_response)) if self.xml_response else None


class WxUser(UserProfileMixin, models.Model):
    auth_user = models.OneToOneField('auth_user.AuthUser', on_delete=models.CASCADE, related_name='wxuser', null=True,
                                     blank=True)
    weixin_id = models.CharField(max_length=32, blank=True)  # 微信号
    # weixin user info
    # https://mp.weixin.qq.com/wiki/14/bb5031008f1494a59c6f71fa0f319c66.html
    # https://mp.weixin.qq.com/wiki/17/c0f37d5704f0b64713d5d2c37b468d75.html
    is_subscribe = models.BooleanField(default=False, blank=False, null=False)  # 用户是否关注公众账号
    nickname = models.CharField(max_length=32, blank=True)
    openid = models.CharField(max_length=64, blank=True)
    sex = models.CharField(max_length=5, blank=True)
    province = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)
    language = models.CharField(max_length=64, blank=True)
    # 用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表640*640正方形头像）
    headimg_url = models.URLField(max_length=256, blank=True)
    privilege = models.CharField(max_length=256, blank=True)
    unionid = models.CharField(max_length=64, blank=True)
    subscribe_time = models.DateField(blank=True, null=True)
    # remark = models.CharField(_('Remark'), max_length=128, blank=True)  # 公众号运营者对粉丝的备注
    groupid = models.CharField(max_length=256, blank=True)  # 用户所在的分组ID
    modified_at = models.DateTimeField('最后更新', auto_now=True, blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    def need_update(self):
        # need update user info every 30 days
        if not self.modified_at:
            return True

        days = 30
        if self.modified_at + relativedelta(days=days) < timezone.now():
            return True
        return False

    def __str__(self):
        return self.nickname