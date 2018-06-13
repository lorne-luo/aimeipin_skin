# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-11 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0014_auto_20180602_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='skintype',
            name='lower_bound',
            field=models.IntegerField(blank=True, null=True, verbose_name='分数下界'),
        ),
        migrations.AddField(
            model_name='skintype',
            name='upper_bound',
            field=models.IntegerField(blank=True, null=True, verbose_name='分数上界'),
        ),
    ]