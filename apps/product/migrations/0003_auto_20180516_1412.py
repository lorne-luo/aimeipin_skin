# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-16 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180512_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pinyin',
            field=models.CharField(blank=True, max_length=512, verbose_name='pinyin'),
        ),
    ]
