# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-27 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20180525_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='sensitivity_score',
        ),
        migrations.AddField(
            model_name='report',
            name='sensitive_score',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='敏感耐受分数'),
        ),
        migrations.AlterField(
            model_name='report',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Answer', verbose_name='调查问卷'),
        ),
        migrations.AlterField(
            model_name='report',
            name='avoid_component',
            field=models.TextField(blank=True, max_length=128, verbose_name='4) 需要避免使用的皮肤护理成分'),
        ),
        migrations.AlterField(
            model_name='report',
            name='day_instruct',
            field=models.CharField(blank=True, max_length=512, verbose_name='日间'),
        ),
        migrations.AlterField(
            model_name='report',
            name='doctor_advice',
            field=models.TextField(blank=True, max_length=128, verbose_name='三、听听皮肤科医生怎么说'),
        ),
        migrations.AlterField(
            model_name='report',
            name='emergency_solution',
            field=models.TextField(blank=True, max_length=128, verbose_name='应急方案'),
        ),
        migrations.AlterField(
            model_name='report',
            name='loose_score',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='易皱纹紧致分数'),
        ),
        migrations.AlterField(
            model_name='report',
            name='loose_type',
            field=models.CharField(blank=True, choices=[('非紧致性', '非紧致性'), ('紧致性', '紧致性')], max_length=64, verbose_name='易皱纹紧致型'),
        ),
        migrations.AlterField(
            model_name='report',
            name='maintain_solution',
            field=models.TextField(blank=True, max_length=128, verbose_name='日常维稳方案'),
        ),
        migrations.AlterField(
            model_name='report',
            name='mask_instruct',
            field=models.CharField(blank=True, max_length=512, verbose_name='面膜'),
        ),
        migrations.AlterField(
            model_name='report',
            name='night_instruct',
            field=models.CharField(blank=True, max_length=512, verbose_name='夜间'),
        ),
        migrations.AlterField(
            model_name='report',
            name='oily_score',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='油干分数'),
        ),
        migrations.AlterField(
            model_name='report',
            name='oily_type',
            field=models.CharField(blank=True, choices=[('重度油性', '重度油性'), ('轻度油性', '轻度油性'), ('轻度干性', '轻度干性'), ('重度干性', '重度干性')], max_length=64, verbose_name='油干类型'),
        ),
        migrations.AlterField(
            model_name='report',
            name='pigment_score',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='色素分数'),
        ),
        migrations.AlterField(
            model_name='report',
            name='pigment_type',
            field=models.CharField(blank=True, choices=[('色素性', '色素性'), ('非色素性', '非色素性')], max_length=64, verbose_name='色素类型'),
        ),
        migrations.AlterField(
            model_name='report',
            name='problem',
            field=models.TextField(blank=True, max_length=128, verbose_name='2. 我们认为您存在的问题'),
        ),
        migrations.AlterField(
            model_name='report',
            name='purpose',
            field=models.CharField(blank=True, choices=[('急镇定', '急镇定'), ('抗轻衰', '抗轻衰'), ('收毛孔', '收毛孔'), ('清痘痘', '清痘痘'), ('祛暗沉', '祛暗沉'), ('调水油', '调水油'), ('种草', '种草')], max_length=64, verbose_name='目标'),
        ),
        migrations.AlterField(
            model_name='report',
            name='sensitive_type',
            field=models.CharField(blank=True, choices=[('重度敏感性', '重度敏感性'), ('轻度敏感性', '轻度敏感性'), ('轻度耐受性', '轻度耐受性'), ('耐受性', '耐受性')], max_length=64, verbose_name='敏感耐受型'),
        ),
        migrations.AlterField(
            model_name='report',
            name='summary',
            field=models.TextField(blank=True, max_length=128, verbose_name='总结'),
        ),
    ]
