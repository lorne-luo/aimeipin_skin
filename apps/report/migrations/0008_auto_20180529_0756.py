# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 23:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_skintype_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='loose_type',
        ),
        migrations.RemoveField(
            model_name='report',
            name='oily_type',
        ),
        migrations.RemoveField(
            model_name='report',
            name='pigment_type',
        ),
        migrations.RemoveField(
            model_name='report',
            name='sensitive_type',
        ),
    ]
