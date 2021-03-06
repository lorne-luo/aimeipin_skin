# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-16 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_auto_20180515_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='loose_type',
            field=models.CharField(blank=True, choices=[('非紧致性', '非紧致性'), ('紧致性', '紧致性')], max_length=64, verbose_name='易皱纹or紧致'),
        ),
        migrations.AlterField(
            model_name='word',
            name='pigment_type',
            field=models.CharField(blank=True, choices=[('色素性', '色素性'), ('非色素性', '非色素性')], max_length=64, verbose_name='色素or非色素'),
        ),
    ]
