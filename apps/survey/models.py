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

    # 记分选择题
    # 12-21 是干油
    question1 = models.PositiveIntegerField(blank=True, null=True) # No. 12
    question2 = models.PositiveIntegerField(blank=True, null=True)  # No. 13
    question3 = models.PositiveIntegerField(blank=True, null=True) # No. 14
    question4 = models.PositiveIntegerField(blank=True, null=True) # No. 15
    question5 = models.PositiveIntegerField(blank=True, null=True) # No. 16
    question6 = models.PositiveIntegerField(blank=True, null=True) # No. 17
    question7 = models.PositiveIntegerField(blank=True, null=True) # No. 18
    question8 = models.PositiveIntegerField(blank=True, null=True) # No. 19
    question9 = models.PositiveIntegerField(blank=True, null=True) # No. 20
    question10 = models.PositiveIntegerField(blank=True, null=True) # No. 21
    # 22-32 是敏感
    question11 = models.PositiveIntegerField(blank=True, null=True) # No. 22
    question12 = models.PositiveIntegerField(blank=True, null=True) # No. 23
    question13 = models.PositiveIntegerField(blank=True, null=True) # No. 24
    question14 = models.PositiveIntegerField(blank=True, null=True) # No. 25
    question15 = models.PositiveIntegerField(blank=True, null=True) # No. 26
    question16 = models.PositiveIntegerField(blank=True, null=True) # No. 27
    question17 = models.PositiveIntegerField(blank=True, null=True) # No. 28
    question18 = models.PositiveIntegerField(blank=True, null=True) # No. 29
    question19 = models.PositiveIntegerField(blank=True, null=True) # No. 30
    question20 = models.PositiveIntegerField(blank=True, null=True) # No. 31
    question21 = models.PositiveIntegerField(blank=True, null=True) # No. 32
    # 33-41 是色素
    question22 = models.PositiveIntegerField(blank=True, null=True) # No. 33
    question23 = models.PositiveIntegerField(blank=True, null=True) # No. 34
    question24 = models.PositiveIntegerField(blank=True, null=True) # No. 35
    question25 = models.PositiveIntegerField(blank=True, null=True) # No. 36
    question26 = models.PositiveIntegerField(blank=True, null=True) # No. 37
    question27 = models.PositiveIntegerField(blank=True, null=True) # No. 38
    question28 = models.PositiveIntegerField(blank=True, null=True) # No. 39
    question29 = models.PositiveIntegerField(blank=True, null=True) # No. 40
    question30 = models.PositiveIntegerField(blank=True, null=True) # No. 41
    # 42-49 是皱纹
    question31 = models.PositiveIntegerField(blank=True, null=True) # No. 42
    question32 = models.PositiveIntegerField(blank=True, null=True) # No. 43
    question33 = models.PositiveIntegerField(blank=True, null=True) # No. 44
    question34 = models.PositiveIntegerField(blank=True, null=True) # No. 45
    question35 = models.PositiveIntegerField(blank=True, null=True) # No. 46
    question36 = models.PositiveIntegerField(blank=True, null=True) # No. 47
    question37 = models.PositiveIntegerField(blank=True, null=True) # No. 48
    question38 = models.PositiveIntegerField(blank=True, null=True) # No. 49

    # 不记分选择题 50-64
    non_score_question1 = models.PositiveIntegerField(blank=True, null=True)  # No. 50
    non_score_question2 = models.PositiveIntegerField(blank=True, null=True)  # No. 51
    non_score_question3 = models.PositiveIntegerField(blank=True, null=True)  # No. 52
    non_score_question4 = models.PositiveIntegerField(blank=True, null=True)  # No. 53
    non_score_question5 = models.PositiveIntegerField(blank=True, null=True)  # No. 54
    non_score_question6 = models.PositiveIntegerField(blank=True, null=True)  # No. 55
    non_score_question7 = models.PositiveIntegerField(blank=True, null=True)  # No. 56
    non_score_question8 = models.PositiveIntegerField(blank=True, null=True)  # No. 57
    non_score_question9 = models.PositiveIntegerField(blank=True, null=True)  # No. 58
    non_score_question10 = models.PositiveIntegerField(blank=True, null=True)  # No. 59
    non_score_question11 = models.PositiveIntegerField(blank=True, null=True)  # No. 60
    non_score_question12 = models.PositiveIntegerField(blank=True, null=True)  # No. 61
    non_score_question13 = models.PositiveIntegerField(blank=True, null=True)  # No. 62
    non_score_question14 = models.PositiveIntegerField(blank=True, null=True)  # No. 63
    non_score_question15 = models.PositiveIntegerField(blank=True, null=True)  # No. 64


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
