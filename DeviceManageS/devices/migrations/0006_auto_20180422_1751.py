# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-22 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20180421_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicerepair',
            name='apply_time',
            field=models.DateField(auto_now=True, null=True, verbose_name='\u7533\u8bf7\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='devicerepair',
            name='category_name',
            field=models.CharField(choices=[('lift_dev', '\u8d77\u91cd\u673a\u68b0'), ('car', '\u6c7d\u8f66')], default='car', max_length=30, verbose_name='\u7c7b\u522b\u540d\u79f0'),
        ),
    ]
