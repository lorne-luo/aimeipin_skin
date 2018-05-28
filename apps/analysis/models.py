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
    description = models.TextField(_('类型'), max_length=128, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_oily_type(score):
        name = ''
        if score:
            if 100 <= score <= 149:
                name = '重度干性'
            elif 150 <= score <= 229:
                name = '轻度干性'
            elif 230 <= score <= 299:
                name = '轻度油性'
            elif 300 <= score <= 400:
                name = '重度油性'
        if name:
            return SkinType.objects.filter(name=name).first()
        return None

    @staticmethod
    def get_sensitive_type(score):
        name = ''
        if score:
            if 110 <= score <= 169:
                name = '耐受性'
            elif 170 <= score <= 269:
                name = '轻度耐受性'
            elif 270 <= score <= 339:
                name = '轻度敏感性'
            elif 340 <= score <= 440:
                name = '重度敏感性'
        if name:
            return SkinType.objects.filter(name=name).first()
        return None

    @staticmethod
    def get_pigment_type(score):
        name = ''
        if score:
            if 60 <= score <= 209:
                name = '非色素性'
            elif 210 <= score <= 360:
                name = '色素性'
        if name:
            return SkinType.objects.filter(name=name).first()
        return None

    @staticmethod
    def get_loose_type(score):
        name = ''
        if score:
            if 100 <= score <= 249:
                name = '紧致性'
            elif 250 <= score <= 400:
                name = '非紧致性'
        if name:
            return SkinType.objects.filter(name=name).first()
        return None


class Word(PinYinFieldModelMixin, models.Model):
    """肤质对应话术, skin_word"""
    purpose = models.CharField(_('目标'), max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标

    oily_type = models.CharField(_('油性or干性'), max_length=64, choices=SKIN_OILY_TYPE_CHOICES, blank=True)
    sensitive_type = models.CharField(_('敏感or耐受'), max_length=64, choices=SKIN_SENSITIVE_TYPE_CHOICES, blank=True)
    pigment_type = models.CharField(_('色素or非色素'), max_length=64, choices=SKIN_PIGMENT_TYPE_CHOICES, blank=True)
    loose_type = models.CharField(_('易皱纹or紧致'), max_length=64, choices=SKIN_LOOSE_TYPE_CHOICES, blank=True)

    oily_type2 = models.ForeignKey('analysis.SkinType',verbose_name=_('油性or干性'), blank=True, null=True,related_name='word_oily_type')
    sensitive_type2 = models.ForeignKey('analysis.SkinType',verbose_name=_('敏感or耐受'), blank=True, null=True,related_name='word_sensitive_type')
    pigment_type2 = models.ForeignKey('analysis.SkinType',verbose_name=_('色素or非色素'), blank=True, null=True,related_name='word_pigment_type')
    loose_type2 = models.ForeignKey('analysis.SkinType',verbose_name=_('易皱纹or紧致'),  blank=True, null=True,related_name='word_loose_type')

    report = models.TextField(_('皮肤检测报告总结'), max_length=512, blank=True)  # 总结报告，填充值问卷报告的总结
    problem = models.TextField(_('我们认为您存在的问题'), max_length=128, blank=True)  # 存在的问题
    avoid_component = models.TextField(_('需要避免使用的皮肤护理成分'), max_length=128, blank=True)  # 避免使用的成分
    doctor_advice = models.TextField(_('听听皮肤科医生怎么说'), max_length=128, blank=True)  # 医生建议
    emergency_solution = models.TextField(_('应急方案'), max_length=128, blank=True)  # 应急方案
    maintain_solution = models.TextField(_('日常维稳方案'), max_length=128, blank=True)  # 维稳方案

    day_instruct = models.CharField(_('日间'), max_length=512, blank=True)  # 日间指导
    night_instruct = models.CharField(_('夜间'), max_length=512, blank=True)  # 夜间指导
    mask_instruct = models.CharField(_('面膜'), max_length=512, blank=True)  # 面膜指导

    pinyin = models.CharField(_(u'pinyin'), max_length=512, blank=True)
    pinyin_fields_conf = [
        ('purpose', Style.NORMAL, False),
        ('oily_type', Style.NORMAL, False),
        ('sensitive_type', Style.NORMAL, False),
        ('pigment_type', Style.NORMAL, False),
        ('loose_type', Style.NORMAL, False),
    ]

    class Meta:
        verbose_name_plural = _('话术')
        verbose_name = _('话术')
