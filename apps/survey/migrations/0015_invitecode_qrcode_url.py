# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0014_answer_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitecode',
            name='qrcode_url',
            field=models.CharField(blank=True, max_length=512, verbose_name='二维码'),
        ),
    ]
