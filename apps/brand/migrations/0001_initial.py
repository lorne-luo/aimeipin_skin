# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-11 04:55
from __future__ import unicode_literals

import apps.brand.models
import core.django.models
from django.db import migrations, models
import django_countries.fields
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
                ('name_en', models.CharField(blank=True, max_length=128, verbose_name='name_en')),
                ('name_cn', models.CharField(blank=True, max_length=128, verbose_name='name_cn')),
                ('pinyin', models.CharField(blank=True, max_length=512, verbose_name='pinyin')),
                ('first_letter_en', models.CharField(blank=True, max_length=128, verbose_name='first_letter_en')),
                ('first_letter_cn', models.CharField(blank=True, max_length=128, verbose_name='first_letter_cn')),
                ('logo', stdimage.models.StdImageField(blank=True, null=True, upload_to='brand', verbose_name='Logo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
            bases=(core.django.models.ResizeUploadedImageModelMixin, core.django.models.PinYinFieldModelMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='brand',
            unique_together=set([('name_en', 'name_cn')]),
        ),
        migrations.AlterIndexTogether(
            name='brand',
            index_together=set([('name_en', 'name_cn')]),
        ),
    ]
