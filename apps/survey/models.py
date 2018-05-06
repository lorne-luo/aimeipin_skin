from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.constants import SEX_CHOICES, INCOME_CHOICES, PURPOSE_CHOICES, SKIN_OILY_TYPE_CHOICES, \
    SKIN_SENSITIVE_TYPE_CHOICES, SKIN_PIGMENT_TYPE_CHOICES, SKIN_LOOSE_TYPE_CHOICES, PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, \
    SURVEY_LEVEL_CHOICES


class Answer(models.Model):
    """问卷报告回答,answer"""
    customer = models.ForeignKey('customer.Customer', null=False, blank=False)
    purpose = models.CharField(max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标
    level = models.CharField(max_length=64, choices=SURVEY_LEVEL_CHOICES, blank=True)  # 9.9 or 98

    # replica of customer basic info
    name = models.CharField(_(u'姓名'), max_length=64, null=False, blank=False)
    sex = models.CharField(_(u'性别'), choices=SEX_CHOICES, max_length=30, null=False, blank=False)
    age = models.PositiveIntegerField(_(u'年龄'), null=True, blank=True)
    email = models.EmailField(_('Email'), max_length=255, blank=True)
    mobile = models.CharField(_(u'手机'), max_length=15, blank=True)
    height = models.PositiveIntegerField(_(u'身高'), null=True, blank=True)
    weight = models.PositiveIntegerField(_(u'体重'), null=True, blank=True)
    job = models.CharField(_(u'职业'), max_length=64, blank=True)
    monthly_income = models.CharField(_(u'收入'), choices=INCOME_CHOICES, max_length=50, blank=True)
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

    # 非选项问题
    allergy = models.TextField(max_length=128, blank=True)  # 过敏

    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)


class Report(models.Model):
    """问卷报告结果, user_content,user_content_word"""
    answer = models.ForeignKey('survey.Answer', null=False, blank=False)
    purpose = models.CharField(max_length=64, choices=PURPOSE_CHOICES,  blank=True)  # 问卷目标
    level = models.CharField(max_length=64, choices=SURVEY_LEVEL_CHOICES,  blank=True)  # 问卷目标

    # 肤质4个维度种类
    oily_type = models.CharField(max_length=64, choices=SKIN_OILY_TYPE_CHOICES, blank=True)
    sensitive_type = models.CharField(max_length=64, choices=SKIN_SENSITIVE_TYPE_CHOICES, blank=True)
    pigment_type = models.CharField(max_length=64, choices=SKIN_PIGMENT_TYPE_CHOICES, blank=True)
    loose_type = models.CharField(max_length=64, choices=SKIN_LOOSE_TYPE_CHOICES, blank=True)
    # 肤质4个维度的测试评分
    oily_score = models.PositiveIntegerField(blank=True, null=True)
    sensitivity_score = models.PositiveIntegerField(blank=True, null=True)
    pigment_score = models.PositiveIntegerField(blank=True, null=True)
    loose_score = models.PositiveIntegerField(blank=True, null=True)

    summary = models.TextField(max_length=128, blank=True)  # 报告总结
    problem = models.TextField(max_length=128, blank=True)  # 存在的问题
    # allergy = models.TextField(max_length=128, blank=True)  # 过敏，copy from answer
    avoid_component = models.TextField(max_length=128, blank=True)  # 避免使用的成分
    doctor_advice = models.TextField(max_length=128, blank=True)  # 医生建议
    day_instruct = models.CharField(max_length=512, blank=True)  # 日间指导
    night_instruct = models.CharField(max_length=512, blank=True)  # 夜间指导
    mask_instruct = models.CharField(max_length=512, blank=True)  # 面膜指导
    emergency_solution = models.TextField(max_length=128, blank=True)  # 应急方案
    maintain_solution = models.TextField(max_length=128, blank=True)  # 维稳方案

    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)


class ReportProductAnalysis(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    product = models.ForeignKey('product.Product', null=False, blank=False)  # 产品外键或名称
    name = models.CharField(max_length=255, blank=True)
    analysis = models.TextField(max_length=128, blank=True)  # 护肤品分析


class ReportProductAdvice(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    type = models.CharField(max_length=64, choices=PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, blank=True)
    product = models.ForeignKey('premium_product.PremiumProduct', null=False, blank=False)
