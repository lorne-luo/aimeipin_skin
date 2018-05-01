from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.constants import SEX_CHOICES, INCOME_CHOICES


class Answer(models.Model):
    customer = models.ForeignKey('customer.Customer', null=False, blank=False)

    # replica of customer basic info
    name = models.CharField(_(u'姓名'), max_length=50, null=False, blank=False)
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

    # selection answer
    question1 = models.PositiveIntegerField(blank=True, null=True)
    question2 = models.PositiveIntegerField(blank=True, null=True)
    question3 = models.PositiveIntegerField(blank=True, null=True)
    question4 = models.PositiveIntegerField(blank=True, null=True)
    question5 = models.PositiveIntegerField(blank=True, null=True)
    question6 = models.PositiveIntegerField(blank=True, null=True)
    question7 = models.PositiveIntegerField(blank=True, null=True)
    question8 = models.PositiveIntegerField(blank=True, null=True)
    question9 = models.PositiveIntegerField(blank=True, null=True)
    question10 = models.PositiveIntegerField(blank=True, null=True)
    question11 = models.PositiveIntegerField(blank=True, null=True)
    question12 = models.PositiveIntegerField(blank=True, null=True)
    question13 = models.PositiveIntegerField(blank=True, null=True)
    question14 = models.PositiveIntegerField(blank=True, null=True)
    question15 = models.PositiveIntegerField(blank=True, null=True)
    question16 = models.PositiveIntegerField(blank=True, null=True)
    question17 = models.PositiveIntegerField(blank=True, null=True)
    question18 = models.PositiveIntegerField(blank=True, null=True)
    question19 = models.PositiveIntegerField(blank=True, null=True)
    question20 = models.PositiveIntegerField(blank=True, null=True)
    question21 = models.PositiveIntegerField(blank=True, null=True)
    question22 = models.PositiveIntegerField(blank=True, null=True)
    question23 = models.PositiveIntegerField(blank=True, null=True)
    question24 = models.PositiveIntegerField(blank=True, null=True)
    question25 = models.PositiveIntegerField(blank=True, null=True)
    question26 = models.PositiveIntegerField(blank=True, null=True)
    question27 = models.PositiveIntegerField(blank=True, null=True)
    question28 = models.PositiveIntegerField(blank=True, null=True)
    question29 = models.PositiveIntegerField(blank=True, null=True)
    question30 = models.PositiveIntegerField(blank=True, null=True)
    question31 = models.PositiveIntegerField(blank=True, null=True)
    question32 = models.PositiveIntegerField(blank=True, null=True)
    question33 = models.PositiveIntegerField(blank=True, null=True)
    question34 = models.PositiveIntegerField(blank=True, null=True)
    question35 = models.PositiveIntegerField(blank=True, null=True)
    question36 = models.PositiveIntegerField(blank=True, null=True)
    question37 = models.PositiveIntegerField(blank=True, null=True)
    question38 = models.PositiveIntegerField(blank=True, null=True)

    # manual input content


class Report(models.Model):
    answer = models.ForeignKey('survey.Answer', null=False, blank=False)
