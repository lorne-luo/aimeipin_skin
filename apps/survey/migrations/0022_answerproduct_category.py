# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0021_auto_20180608_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerproduct',
            name='category',
            field=models.CharField(blank=True, choices=[('卸妆', '卸妆'), ('洁面', '洁面'), ('化妆水', '化妆水'), ('乳液/面霜', '乳液/面霜'), ('精华', '精华'), ('去角质', '去角质'), ('面膜', '面膜'), ('防晒', '防晒')], max_length=64),
        ),
    ]
