# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-27 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20180527_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='allergy',
            field=models.TextField(blank=True, max_length=128, verbose_name='过敏'),
        ),
    ]