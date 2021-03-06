# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypinyin import Style
from config.constants import (SKIN_OILY_TYPE_CHOICES, SKIN_SENSITIVE_TYPE_CHOICES, SKIN_PIGMENT_TYPE_CHOICES,
                              SKIN_LOOSE_TYPE_CHOICES, PURPOSE_CHOICES, SKIN_TYPE_DIMENSION_CHOICES)
from core.django.models import PinYinFieldModelMixin


class SkinType(models.Model):
    dimension = models.CharField(_('维度'), max_length=64, choices=SKIN_TYPE_DIMENSION_CHOICES, blank=True)
    name = models.CharField(_('名称'), max_length=64,
                            choices=SKIN_OILY_TYPE_CHOICES + SKIN_SENSITIVE_TYPE_CHOICES + SKIN_PIGMENT_TYPE_CHOICES + SKIN_LOOSE_TYPE_CHOICES,
                            blank=True)
    short_name = models.CharField(_('简称'), max_length=64, blank=True)
    lower_bound = models.IntegerField(_('分数下界'), blank=True, null=True)
    upper_bound = models.IntegerField(_('分数上界'), blank=True, null=True)
    short_description = models.TextField(_('简评'), max_length=512, blank=True)
    description = models.TextField(_('备注'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("dimension", "name")

    @staticmethod
    def get_oily_type(score):
        if score:
            for t in SkinType.objects.filter(dimension='油性or干性'):
                if t.lower_bound <= score <= t.upper_bound:
                    return t
        return None

    @staticmethod
    def get_sensitive_type(score):
        if score:
            for t in SkinType.objects.filter(dimension='敏感or耐受'):
                if t.lower_bound <= score <= t.upper_bound:
                    return t
        return None

    @staticmethod
    def get_pigment_type(score):
        if score:
            for t in SkinType.objects.filter(dimension='色素or非色素'):
                if t.lower_bound <= score <= t.upper_bound:
                    return t
        return None

    @staticmethod
    def get_loose_type(score):
        if score:
            for t in SkinType.objects.filter(dimension='易皱纹or紧致'):
                if t.lower_bound <= score <= t.upper_bound:
                    return t
        return None


class Word(PinYinFieldModelMixin, models.Model):
    """肤质对应话术, skin_word"""
    purpose = models.CharField(_('目标'), max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标
    oily_type = models.ForeignKey('analysis.SkinType', verbose_name=_('油性or干性'), blank=True, null=True,
                                  related_name='word_oily_type')
    sensitive_type = models.ForeignKey('analysis.SkinType', verbose_name=_('敏感or耐受'), blank=True, null=True,
                                       related_name='word_sensitive_type')
    pigment_type = models.ForeignKey('analysis.SkinType', verbose_name=_('色素or非色素'), blank=True, null=True,
                                     related_name='word_pigment_type')
    loose_type = models.ForeignKey('analysis.SkinType', verbose_name=_('易皱纹or紧致'), blank=True, null=True,
                                   related_name='word_loose_type')

    report = models.TextField(_('皮肤检测报告总结'), blank=True)  # 总结报告，填充值问卷报告的总结
    problem = models.TextField(_('我们认为您存在的问题'), blank=True)  # 存在的问题
    avoid_component = models.TextField(_('需要避免使用的皮肤护理成分'), blank=True)  # 避免使用的成分
    doctor_advice = models.TextField(_('听听皮肤科医生怎么说'), blank=True)  # 医生建议
    emergency_solution = models.TextField(_('应急方案'), blank=True)  # 应急方案
    maintain_solution = models.TextField(_('日常维稳方案'), blank=True)  # 维稳方案

    day_instruct = models.TextField(_('日间'), blank=True)  # 日间指导
    night_instruct = models.TextField(_('夜间'), blank=True)  # 夜间指导
    mask_instruct = models.TextField(_('面膜'), blank=True)  # 面膜指导

    pinyin = models.CharField(_(u'pinyin'), max_length=1024, blank=True)
    pinyin_fields_conf = [
        ('purpose', Style.NORMAL, False),
        ('oily_type__name', Style.NORMAL, False),
        ('sensitive_type__name', Style.NORMAL, False),
        ('pigment_type__name', Style.NORMAL, False),
        ('loose_type__name', Style.NORMAL, False),
    ]

    class Meta:
        verbose_name_plural = _('话术')
        verbose_name = _('话术')
        unique_together = (('purpose', 'oily_type', 'sensitive_type', 'pigment_type', 'loose_type'),)

    def __str__(self):
        return '%s-%s_%s_%s_%s' % (
        self.purpose, self.oily_type, self.sensitive_type, self.pigment_type, self.loose_type)
