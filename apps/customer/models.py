# coding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypinyin import pinyin, lazy_pinyin, Style
from config.constants import INCOME_CHOICES, SEX_CHOICES
from core.django.models import PinYinFieldModelMixin


class Customer(models.Model):
    """顾客信息，user_data"""
    wx_user = models.ForeignKey('weixin.WxUser', null=True, blank=True)
    name = models.CharField(_(u'姓名'), max_length=64, blank=False)
    name_py = models.CharField(_(u'姓名'), max_length=50, blank=True)
    sex = models.CharField(_(u'性别'), choices=SEX_CHOICES, max_length=30, blank=False)
    age = models.PositiveIntegerField(_(u'年龄'), null=True, blank=True)
    email = models.EmailField(_('Email'), max_length=255, blank=True)
    mobile = models.CharField(_(u'手机'), max_length=15, blank=True)
    height = models.PositiveIntegerField(_(u'身高'), null=True, blank=True)
    weight = models.PositiveIntegerField(_(u'体重'), null=True, blank=True)
    job = models.CharField(_(u'职业'), max_length=64, blank=True)
    monthly_income = models.CharField(_(u'收入'), choices=INCOME_CHOICES, max_length=50, blank=True)
    weixin_id = models.CharField(_(u'微信号'), max_length=128, blank=True)
    address = models.CharField(_(u'地址'), max_length=255, blank=True)
    remark = models.CharField(_(u'备注'), max_length=255, blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        verbose_name_plural = _('Customer')
        verbose_name = _('Customer')

    def __str__(self):
        return '%s' % self.name

    def send_email(self, subject, message):
        if self.email:
            # todo send email
            pass

    def send_sms(self, content, app_name=None):
        if self.mobile:
            # todo send sms for china mobile number
            pass

    def save(self, *args, **kwargs):
        pinyin_list = PinYinFieldModelMixin.get_combinations(pinyin(self.name, heteronym=True))
        self.name_py = ' '.join(pinyin_list)
        super(Customer, self).save(*args, **kwargs)
