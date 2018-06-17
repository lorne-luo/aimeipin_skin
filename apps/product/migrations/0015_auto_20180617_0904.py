# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-17 01:04
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20180612_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=stdimage.utils.UploadToClassNameDir(), verbose_name='picture'),
        ),
    ]