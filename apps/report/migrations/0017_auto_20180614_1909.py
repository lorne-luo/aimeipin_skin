# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-14 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0016_auto_20180614_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportproductanalysis',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reportproductanalysis',
            name='report',
        ),
        migrations.DeleteModel(
            name='ReportProductAnalysis',
        ),
    ]
