# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_auto_20180529_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='day_instruct',
            field=models.CharField(blank=True, max_length=512, verbose_name='日间'),
        ),
        migrations.AddField(
            model_name='report',
            name='mask_instruct',
            field=models.CharField(blank=True, max_length=512, verbose_name='面膜'),
        ),
        migrations.AddField(
            model_name='report',
            name='night_instruct',
            field=models.CharField(blank=True, max_length=512, verbose_name='夜间'),
        ),
    ]