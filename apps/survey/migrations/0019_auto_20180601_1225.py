# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-01 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0018_answer_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerproduct',
            name='analysis',
            field=models.TextField(blank=True, max_length=255, verbose_name='product analysis'),
        ),
        migrations.AlterField(
            model_name='answerproduct',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='product name'),
        ),
    ]
