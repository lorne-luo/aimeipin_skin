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


class Word(PinYinFieldModelMixin, models.Model):
    """肤质对应话术, skin_word"""
    purpose = models.CharField(_('目标'), max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标

    oily_type = models.CharField(_('油性or干性'), max_length=64, choices=SKIN_OILY_TYPE_CHOICES, blank=True)
    sensitive_type = models.CharField(_('敏感or耐受'), max_length=64, choices=SKIN_SENSITIVE_TYPE_CHOICES, blank=True)
    pigment_type = models.CharField(_('色素or非色素'), max_length=64, choices=SKIN_PIGMENT_TYPE_CHOICES, blank=True)
    loose_type = models.CharField(_('易皱纹or紧致'), max_length=64, choices=SKIN_LOOSE_TYPE_CHOICES, blank=True)

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
