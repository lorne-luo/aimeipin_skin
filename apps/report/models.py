from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.analysis.models import SkinType
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
    oily_type = models.ForeignKey('analysis.SkinType', verbose_name=_('油性or干性'), blank=True, null=True,
                                  related_name='report_oily_type')
    sensitive_type = models.ForeignKey('analysis.SkinType', verbose_name=_('敏感or耐受'), blank=True, null=True,
                                       related_name='report_sensitive_type')
    pigment_type = models.ForeignKey('analysis.SkinType', verbose_name=_('色素or非色素'), blank=True, null=True,
                                     related_name='report_pigment_type')
    loose_type = models.ForeignKey('analysis.SkinType', verbose_name=_('易皱纹or紧致'), blank=True, null=True,
                                   related_name='report_loose_type')

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
    remark = models.TextField('温馨提示', max_length=128, blank=True)  # 温馨提示, for 9.9

    modified_at = models.DateTimeField('最后更新', auto_now=True, blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    def classify_skin_type(self):
        self.oily_score = self.answer.oily_score
        self.sensitive_score = self.answer.sensitive_score
        self.pigment_score = self.answer.pigment_score
        self.loose_score = self.answer.loose_score

        self.oily_type = SkinType.get_oily_type(self.oily_score)
        self.sensitive_type = SkinType.get_sensitive_type(self.sensitive_score)
        self.pigment_type = SkinType.get_pigment_type(self.pigment_score)
        self.loose_type = SkinType.get_loose_type(self.loose_score)

    def save(self, *args, **kwargs):
        super(Report, self).save(*args, **kwargs)

    def generate(self):
        self.classify_skin_type()
        self.allergy = self.answer.other_question2
        self.save()

    def __str__(self):
        return '%s %s#%s' % (self.answer.name, self.purpose, self.level)


class ReportProductAnalysis(models.Model):
    '''用户使用产品的分析 user_product_txt'''
    report = models.ForeignKey(Report, null=False, blank=False)
    product = models.ForeignKey('product.Product', null=False, blank=False)  # 产品外键或名称
    name = models.CharField(max_length=255, blank=True)
    analysis = models.TextField(max_length=128, blank=True)  # 护肤品分析


class ReportPremiumProduct(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    type = models.CharField(max_length=64, choices=PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, blank=True)
    product = models.ForeignKey('premium_product.PremiumProduct', null=False, blank=False)

    def __str__(self):
        return '%s @ %s %s' % (self.product, self.report, self.type)
