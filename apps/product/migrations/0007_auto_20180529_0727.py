# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0008_auto_20180529_0727'),
        ('product', '0006_auto_20180517_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='productanalysis',
            name='loose_type2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_analysis_loose_type', to='analysis.SkinType', verbose_name='易皱纹or紧致'),
        ),
        migrations.AddField(
            model_name='productanalysis',
            name='oily_type2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_analysis_oily_type', to='analysis.SkinType', verbose_name='油性or干性'),
        ),
        migrations.AddField(
            model_name='productanalysis',
            name='pigment_type2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_analysis_pigment_type', to='analysis.SkinType', verbose_name='色素or非色素'),
        ),
        migrations.AddField(
            model_name='productanalysis',
            name='sensitive_type2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_analysis_sensitive_type', to='analysis.SkinType', verbose_name='敏感or耐受'),
        ),
    ]
