# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-07 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def forward(apps, schema_editor):
    AnswerProduct = apps.get_model('survey', 'AnswerProduct')
    for p in AnswerProduct.objects.all():
        if p.cosmetic_products1.count():
            p.answer = p.cosmetic_products1.first()
            p.type = '卸妆'
            p.save()
            continue
        if p.cosmetic_products2.count():
            p.answer = p.cosmetic_products2.first()
            p.type = '洁面'
            p.save()
            continue
        if p.cosmetic_products3.count():
            p.answer = p.cosmetic_products3.first()
            p.type = '化妆'
            p.save()
            continue
        if p.cosmetic_products4.count():
            p.answer = p.cosmetic_products4.first()
            p.type = '面霜'
            p.save()
            continue
        if p.cosmetic_products5.count():
            p.answer = p.cosmetic_products5.first()
            p.type = '精华'
            p.save()
            continue
        if p.cosmetic_products6.count():
            p.answer = p.cosmetic_products6.first()
            p.type = '去角质'
            p.save()
            continue
        if p.cosmetic_products7.count():
            p.answer = p.cosmetic_products7.first()
            p.type = '面膜'
            p.save()
            continue
        if p.cosmetic_products8.count():
            p.answer = p.cosmetic_products8.first()
            p.type = '防晒'
            p.save()
            continue

def backward(apps, schema_editor):
    # do nothing
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0019_auto_20180601_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerproduct',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Answer'),
        ),
        migrations.AddField(
            model_name='answerproduct',
            name='type',
            field=models.CharField(blank=True, choices=[('卸妆', '卸妆'), ('洁面', '洁面'), ('化妆', '化妆'), ('面霜', '面霜'), ('精华', '精华'), ('去角质', '去角质'), ('面膜', '面膜'), ('防晒', '防晒')], max_length=64, verbose_name='type'),
        ),
        # migrations.RunPython(forward, backward)
    ]
