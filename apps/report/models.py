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
    oily_type = models.CharField('油干类型', max_length=64, choices=SKIN_OILY_TYPE_CHOICES, blank=True)
    sensitive_type = models.CharField('敏感耐受型', max_length=64, choices=SKIN_SENSITIVE_TYPE_CHOICES, blank=True)
    pigment_type = models.CharField('色素类型', max_length=64, choices=SKIN_PIGMENT_TYPE_CHOICES, blank=True)
    loose_type = models.CharField('易皱纹紧致型', max_length=64, choices=SKIN_LOOSE_TYPE_CHOICES, blank=True)
    # 肤质4个维度的测试评分
    oily_score = models.PositiveIntegerField('油干分数', blank=True, null=True)
    sensitive_score = models.PositiveIntegerField('敏感耐受分数', blank=True, null=True)
    pigment_score = models.PositiveIntegerField('色素分数', blank=True, null=True)
    loose_score = models.PositiveIntegerField('易皱纹紧致分数', blank=True, null=True)

    summary = models.TextField('总结', max_length=128, blank=True)  # 报告总结
    problem = models.TextField('2. 我们认为您存在的问题', max_length=128, blank=True)  # 存在的问题
    avoid_component = models.TextField('4) 需要避免使用的皮肤护理成分', max_length=128, blank=True)  # 避免使用的成分
    doctor_advice = models.TextField('三、听听皮肤科医生怎么说', max_length=128, blank=True)  # 医生建议
    day_instruct = models.CharField('日间', max_length=512, blank=True)  # 日间指导
    night_instruct = models.CharField('夜间', max_length=512, blank=True)  # 夜间指导
    mask_instruct = models.CharField('面膜', max_length=512, blank=True)  # 面膜指导
    emergency_solution = models.TextField('应急方案', max_length=128, blank=True)  # 应急方案
    maintain_solution = models.TextField('日常维稳方案', max_length=128, blank=True)  # 维稳方案
    allergy = models.TextField('过敏', max_length=128, blank=True)  # 过敏, answer.other_question2
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    def classify_skin_type(self):
        self.oily_score = self.answer.oily_score
        self.sensitive_score = self.answer.sensitive_score
        self.pigment_score = self.answer.pigment_score
        self.loose_score = self.answer.loose_score

        if self.oily_score:
            if 100 <= self.oily_score <= 149:
                self.oily_type = '重度干性'
            elif 150 <= self.oily_score <= 229:
                self.oily_type = '轻度干性'
            elif 230 <= self.oily_score <= 299:
                self.oily_type = '轻度油性'
            elif 300 <= self.oily_score <= 400:
                self.oily_type = '重度油性'

        if self.sensitive_score:
            if 110 <= self.sensitive_score <= 169:
                self.sensitive_type = '耐受性'
            elif 170 <= self.sensitive_score <= 269:
                self.sensitive_type = '轻度耐受性'
            elif 270 <= self.sensitive_score <= 339:
                self.sensitive_type = '轻度敏感性'
            elif 340 <= self.sensitive_score <= 440:
                self.sensitive_type = '重度敏感性'

        if self.pigment_score:
            if 60 <= self.pigment_score <= 209:
                self.pigment_type = '非色素性'
            elif 210 <= self.pigment_score <= 360:
                self.pigment_type = '色素性'

        if self.loose_score:
            if 100 <= self.loose_score <= 249:
                self.loose_type = '紧致性'
            elif 250 <= self.loose_score <= 400:
                self.loose_type = '非紧致性'

    def save(self, *args, **kwargs):
        super(Report, self).save(*args, **kwargs)

    def generate(self):
        self.classify_skin_type()
        self.allergy = self.answer.other_question2
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
