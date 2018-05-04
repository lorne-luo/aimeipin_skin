# coding=utf-8

from django.db import models

from config.constants import (SKIN_OIL_OR_DRY_CHOICES, SKIN_SENSITIVITY_CHOICES, SKIN_PIGMENT_CHOICES,
                              SKIN_LOOSE_CHOICES, PURPOSE_CHOICES)


class Word(models.Model):
    """肤质对应话术, skin_word"""
    purpose = models.CharField(max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标

    oil_or_dry = models.CharField(max_length=64, choices=SKIN_OIL_OR_DRY_CHOICES, blank=True)
    sensitivity = models.CharField(max_length=64, choices=SKIN_SENSITIVITY_CHOICES, blank=True)
    pigment = models.CharField(max_length=64, choices=SKIN_PIGMENT_CHOICES, blank=True)
    loose = models.CharField(max_length=64, choices=SKIN_LOOSE_CHOICES, blank=True)

    report = models.TextField(max_length=512, blank=True)  # 总结报告，填充值问卷报告的总结
    avoid_component = models.TextField(max_length=128, blank=True)  # 避免使用的成分
    doctor_advice = models.TextField(max_length=128, blank=True)  # 医生建议
    emergency_solution = models.TextField(max_length=128, blank=True)  # 应急方案
    maintain_solution = models.TextField(max_length=128, blank=True)  # 维稳方案

    day_instruct = models.CharField(max_length=512, blank=True)  # 日间指导
    night_instruct = models.CharField(max_length=512, blank=True)  # 夜间指导
    mask_instruct = models.CharField(max_length=512, blank=True)  # 面膜指导
    problem = models.TextField(max_length=128, blank=True)  # 存在的问题
