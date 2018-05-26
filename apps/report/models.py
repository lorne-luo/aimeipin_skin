from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.constants import SEX_CHOICES, INCOME_CHOICES, PURPOSE_CHOICES, SKIN_OILY_TYPE_CHOICES, \
    SKIN_SENSITIVE_TYPE_CHOICES, SKIN_PIGMENT_TYPE_CHOICES, SKIN_LOOSE_TYPE_CHOICES, \
    PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, \
    SURVEY_LEVEL_CHOICES


class Report(models.Model):
    """问卷报告结果, user_content,user_content_word"""
    answer = models.ForeignKey('survey.Answer', null=False, blank=False, verbose_name='调查问卷')
    purpose = models.CharField('目标', max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标
    level = models.CharField('价位', max_length=64, choices=SURVEY_LEVEL_CHOICES, blank=True)  # 价位

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
    avoid_component = models.TextField(max_length=128, blank=True)  # 避免使用的成分
    doctor_advice = models.TextField(max_length=128, blank=True)  # 医生建议
    day_instruct = models.CharField(max_length=512, blank=True)  # 日间指导
    night_instruct = models.CharField(max_length=512, blank=True)  # 夜间指导
    mask_instruct = models.CharField(max_length=512, blank=True)  # 面膜指导
    emergency_solution = models.TextField(max_length=128, blank=True)  # 应急方案
    maintain_solution = models.TextField(max_length=128, blank=True)  # 维稳方案

    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    def generate(self):
        self.save()


class ReportProductAnalysis(models.Model):
    '''用户使用产品的分析 user_product_txt'''
    report = models.ForeignKey(Report, null=False, blank=False)
    product = models.ForeignKey('product.Product', null=False, blank=False)  # 产品外键或名称
    name = models.CharField(max_length=255, blank=True)
    analysis = models.TextField(max_length=128, blank=True)  # 护肤品分析


class ReportProductAdvice(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    type = models.CharField(max_length=64, choices=PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, blank=True)
    product = models.ForeignKey('premium_product.PremiumProduct', null=False, blank=False)
