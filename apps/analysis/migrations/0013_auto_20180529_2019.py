# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-29 12:19
from __future__ import unicode_literals

from django.db import migrations, models


def forward(apps, schema_editor):
    SkinType = apps.get_model('analysis', 'SkinType')
    for s in SkinType.objects.all():
        s.short_description = '您属于%s肌肤' % s.name
        s.save()


def backward(apps, schema_editor):
    # do nothing
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('analysis', '0012_auto_20180529_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='skintype',
            name='short_description',
            field=models.TextField(blank=True, max_length=255, verbose_name='简评'),
        ),
        migrations.AlterField(
            model_name='skintype',
            name='description',
            field=models.TextField(blank=True, max_length=512, verbose_name='备注'),
        ),
        migrations.RunPython(forward, backward)
    ]