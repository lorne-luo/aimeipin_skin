# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-12 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='pinyin',
            field=models.CharField(blank=True, max_length=512, verbose_name='pinyin'),
        ),
        migrations.AlterField(
            model_name='word',
            name='loose_type',
            field=models.CharField(blank=True, choices=[('非紧致性皮肤', '非紧致性皮肤'), ('紧致性皮肤', '紧致性皮肤')], max_length=64),
        ),
        migrations.AlterField(
            model_name='word',
            name='oily_type',
            field=models.CharField(blank=True, choices=[('重度油性', '重度油性'), ('轻度油性', '轻度油性'), ('轻度干性', '轻度干性'), ('重度干性', '重度干性')], max_length=64),
        ),
        migrations.AlterField(
            model_name='word',
            name='pigment_type',
            field=models.CharField(blank=True, choices=[('色素性皮肤', '色素性皮肤'), ('非色素性皮肤', '非色素性皮肤')], max_length=64),
        ),
        migrations.AlterField(
            model_name='word',
            name='sensitive_type',
            field=models.CharField(blank=True, choices=[('重度敏感性', '重度敏感性'), ('轻度敏感性', '轻度敏感性'), ('轻度耐受性', '轻度耐受性'), ('耐受性', '耐受性')], max_length=64),
        ),
    ]
