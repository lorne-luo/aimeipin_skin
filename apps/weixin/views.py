# coding=utf-8
import json
import logging
import unicodedata

from braces.views import SuperuserRequiredMixin
from django.contrib.auth import login
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.utils import timezone
from django.conf import settings
from django.utils.http import urlunquote, urlquote
from django.views.generic import ListView, UpdateView
from weixin import WeixinPay
from weixin.base import Map
from weixin.login import WeixinLogin

from apps.survey.models import Answer
from core.django.views import CommonContextMixin
from core.auth_user.models import AuthUser
from . import forms
from . import conf
from .models import WxReturnCode, WxUser

log = logging.getLogger(__name__)


# views for Customer

class WxUserListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    model = WxUser
    template_name_suffix = '_list'  # customer/customer_list.html


class WxUserDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    model = WxUser
    form_class = forms.WxUserDetailForm
    template_name = 'adminlte/common_detail.html'


def wx_login(request):
    next_url = request.GET.get('next', '')
    next_url = urlunquote(next_url)

    if request.user.is_authenticated():
        if next_url:
            return HttpResponseRedirect(next_url)
        else:
            raise Http404

    full_url = '%s%s' % (settings.BASE_URL, reverse('weixin:auth'))
    wx_login = WeixinLogin(conf.APP_ID, conf.APP_SECRET)
    login_url = wx_login.authorize(full_url, conf.SCOPE_USERINFO, urlquote(next_url))
    log.info('weixin login_url: %s' % (login_url))
    return HttpResponseRedirect(login_url)


def wx_auth(request):
    code = request.GET.get("code", None)
    if code is None:
        return HttpResponse('No Code Provided.')

    wx_login = WeixinLogin(conf.APP_ID, conf.APP_SECRET)
    data = wx_login.access_token(code)

    openid = data.openid
    scope = data.scope
    token = data.access_token  # 网页授权access_token和公众号的access_token不一样
    # 关于网页授权access_token和普通access_token的区别
    # 1、微信网页授权是通过OAuth2.0机制实现的，在用户授权给公众号后，公众号可以获取到一个网页授权特有的接口调用凭证（网页授权access_token），通过网页授权access_token可以进行授权后接口调用，如获取用户基本信息；
    # 2、其他微信接口，需要通过基础支持中的“获取access_token”接口来获取到的普通access_token调用。

    wx_user, created = WxUser.objects.get_or_create(openid=openid)

    if created or wx_user.need_update():
        # continue to get userinfo
        userinfo = wx_login.user_info(token, openid)
        wx_user = WxUser.objects.filter(openid=openid).first() or WxUser()
        # update user info
        wx_user.openid = openid
        nickname = userinfo.nickname
        nickname = ''.join(c for c in unicodedata.normalize('NFC', nickname) if c <= '\uFFFF')  # remove emoji
        wx_user.nickname = nickname
        wx_user.headimg_url = userinfo.headimgurl
        wx_user.sex = userinfo.sex
        wx_user.province = userinfo.province
        wx_user.city = userinfo.city
        wx_user.country = userinfo.country
        wx_user.unionid = userinfo.get('unionid', '')
        wx_user.privilege = json.dumps(userinfo.privilege)
        wx_user.language = userinfo.language
        wx_user.save()

        # 关于UnionID机制
        # 1、请注意，网页授权获取用户基本信息也遵循UnionID机制。即如果开发者有在多个公众号，或在公众号、移动应用之间统一用户帐号的需求，需要前往微信开放平台（open.weixin.qq.com）绑定公众号后，才可利用UnionID机制来满足上述需求。
        # 2、UnionID机制的作用说明：如果开发者拥有多个移动应用、网站应用和公众帐号，可通过获取用户基本信息中的unionid来区分用户的唯一性，因为同一用户，对同一个微信开放平台下的不同应用（移动应用、网站应用和公众帐号），unionid是相同的。

    user = wx_user.auth_user
    if not user:
        user = AuthUser.objects.filter(username=wx_user.openid).first()
        if not user:
            user = AuthUser.objects.create_user(username=wx_user.openid, password=wx_user.openid)
        wx_user.auth_user = user
        wx_user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    request.session['wx_openid'] = openid

    state = request.GET.get('state', None)
    if state:
        url = urlunquote(state)
    else:
        url = reverse('weixin:index')

    return HttpResponseRedirect(url)


def wx_index(request):
    return HttpResponse('test page')


def wx_pay_notify(request):
    full_url = '%s%s' % (settings.BASE_URL, reverse('weixin:pay_notify'))
    weixin_pay = WeixinPay(conf.APP_ID, conf.MCH_ID, conf.MCH_KEY, full_url)

    result = Map(weixin_pay.to_dict(request.body))

    if not weixin_pay.check(result):
        return JsonResponse({'return_code': WxReturnCode.FAIL,
                             'return_msg': '签名验证失败'})

    # todo create weixin payment based on Order
    # try:
    #     order = Order.objects.get(code=result.out_trade_no)
    # except:
    #     log.error('[Paymen Notify] OrderID = %s not found' % result.out_trade_no)
    #     raise Http404
    #
    # wx_payment = WxPayment(order=order, return_code=result.return_code, return_msg=result.return_msg,
    #                        result_code=result.result_code, appid=result.appid, mch_id=result.mch_id,
    #                        device_info=result.device_info, nonce_str=result.nonce_str, sign=result.sign,
    #                        sign_type=result.sign_type, err_code=result.err_code, err_code_des=result.err_code_des,
    #                        openid=result.openid, is_subscribe=result.is_subscribe, trade_type=result.trade_type,
    #                        bank_type=result.bank_type, total_fee=result.total_fee, fee_type=result.fee_type,
    #                        attach=result.attach, time_end=result.time_end,
    #                        transaction_id=result.transaction_id, xml_response=request.body)
    # wx_payment.save()
    #
    # if wx_payment.is_success:
    #     wx_payment.order.is_paid = True
    #     wx_payment.order.paid_time = timezone.now()
    #     wx_payment.order.save(update_fields=['is_paid', 'paid_time'])
    #
    # wx_user = WxUser.objects.filter(openid=wx_payment.openid).first()
    # if wx_user:
    #     wx_user.is_subscribe = wx_payment.is_subscribe
    #     wx_user.save(update_fields=['is_subscribe'])

    return JsonResponse({'return_code': WxReturnCode.SUCCESS,
                         'return_msg': 'OK'})
