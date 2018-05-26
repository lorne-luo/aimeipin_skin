# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-26 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_auto_20180525_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitecode',
            old_name='code',
            new_name='uuid',
        ),
        migrations.AddField(
            model_name='answer',
            name='uuid',
            field=models.CharField(blank=True, max_length=64, verbose_name='uuid'),
        ),
    ]
