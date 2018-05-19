# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-19 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20180515_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='fill_blank_question5',
            new_name='cosmetic_question5',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='fill_blank_question10',
            new_name='other_question2',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question1',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question2',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question3',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question4',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question6',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question7',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question8',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='fill_blank_question9',
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetic_question1',
            field=models.TextField(blank=True, max_length=255, verbose_name='65. 目前正在使用的卸妆类的护肤品名)：'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetic_question2',
            field=models.TextField(blank=True, max_length=255, verbose_name='66、目前正在使用的洁面乳/洁面霜/洁面油类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetic_question3',
            field=models.TextField(blank=True, max_length=255, verbose_name='67、目前正在所使用化妆水类护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetic_question4',
            field=models.TextField(blank=True, max_length=255, verbose_name='68、目前正在所使用乳液／面霜类护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetic_question6',
            field=models.TextField(blank=True, max_length=255, verbose_name='70、目前正在使用的去角质类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetic_question7',
            field=models.TextField(blank=True, max_length=255, verbose_name='71、目前正在使用的的面膜类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetic_question8',
            field=models.TextField(blank=True, max_length=255, verbose_name='72、目前正在使用的防晒类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='is_changeable',
            field=models.BooleanField(default=False, verbose_name='是否可修改'),
        ),
        migrations.AddField(
            model_name='answer',
            name='other_question1',
            field=models.TextField(blank=True, max_length=255, verbose_name='73、您是否每天（一年四季，不管晴天、阴天、雨天，室内室外）涂抹足量（面部一元硬币大小）专门的防晒产品（不包括隔离霜，底妆）？'),
        ),
        migrations.AddField(
            model_name='answer',
            name='uuid',
            field=models.CharField(blank=True, max_length=255, verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='non_score_question15',
            field=models.CharField(blank=True, max_length=255, verbose_name='64. 近半年内您是否有出现过严重的皮肤问题(例如：大面积的痤疮. 湿疹. 皮肤过敏),请详细描述具体情况：'),
        ),
    ]
