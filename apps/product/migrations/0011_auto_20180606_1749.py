# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20180529_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productanalysis',
            name='analysis',
            field=models.TextField(blank=True, max_length=1024, verbose_name='对应阐述'),
        ),
        migrations.AlterField(
            model_name='productingredient',
            name='effect',
            field=models.CharField(blank=True, max_length=512, verbose_name='使用目的'),
        ),
    ]