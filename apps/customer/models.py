# coding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.auth_user.models import AuthUser, UserProfileMixin
from config.constants import INCOME_CHOICES, SEX_CHOICES
from apps.product.models import Product


class Customer( models.Model):
    wx_user=models.ForeignKey('weixin.WxUser', null=True, blank=True)
    name = models.CharField(_(u'姓名'), max_length=50, null=False, blank=False)
    name_py = models.CharField(_(u'姓名'), max_length=50, null=True, blank=True)
    sex = models.CharField(_(u'性别'), choices=SEX_CHOICES, max_length=30, null=False, blank=False)
    age = models.PositiveIntegerField(_(u'年龄'), null=True, blank=True)
    email = models.EmailField(_('Email'), max_length=255, blank=True)
    mobile = models.CharField(_(u'手机'), max_length=15, blank=True)
    height = models.PositiveIntegerField(_(u'身高'), null=True, blank=True)
    weight = models.PositiveIntegerField(_(u'体重'), null=True, blank=True)
    job = models.CharField(_(u'职业'), max_length=50, null=True, blank=True)
    monthly_income = models.CharField(_(u'收入'), choices=INCOME_CHOICES, max_length=50, null=True,
                                      blank=True)  # todo choice
    weixin_id = models.CharField(_(u'微信号'), max_length=128, blank=True)
    address = models.CharField(_(u'地址'), max_length=255, blank=True)
    remark = models.CharField(_(u'备注'), max_length=255, blank=True)

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
        # todo send sms for china mobile number
        pass
