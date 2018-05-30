# coding=utf-8

from django.db import models

from config.constants import (SKIN_OILY_TYPE_CHOICES, SKIN_SENSITIVE_TYPE_CHOICES, SKIN_PIGMENT_TYPE_CHOICES,
                              SKIN_LOOSE_TYPE_CHOICES, PURPOSE_CHOICES)


class Purpose(models.Model):
    """目标"""
    name = models.CharField(max_length=64, blank=True)  # 目标名称

    def __str__(self):
        return self.name
#
# class SkinTypeOily(models.Model):
#     """目标"""
#     name = models.CharField(max_length=64, blank=True)  # 名称
#
#     def __str__(self):
#         return self.name
#
#
# class SkinTypeSensitive(models.Model):
#     """目标"""
#     name = models.CharField(max_length=64, blank=True)  # 名称
#
#     def __str__(self):
#         return self.name
#
#
# class SkinTypePigment(models.Model):
#     """目标"""
#     name = models.CharField(max_length=64, blank=True)  # 名称
#
#     def __str__(self):
#         return self.name
#
#
# class SkinTypeLoose(models.Model):
#     """目标"""
#     name = models.CharField(max_length=64, blank=True)  # 名称
#
#     def __str__(self):
#         return self.name
#
