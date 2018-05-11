# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-11 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceRepair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_id', models.CharField(max_length=20, verbose_name='\u7533\u8bf7\u7f16\u53f7')),
                ('device_id', models.CharField(max_length=20, verbose_name='\u8bbe\u5907\u7f16\u53f7')),
                ('device_name', models.CharField(max_length=10, verbose_name='\u8bbe\u5907\u540d\u79f0')),
                ('category_name', models.CharField(choices=[('lift_dev', '\u8d77\u91cd\u673a\u68b0'), ('car', '\u6c7d\u8f66')], default='car', max_length=30, verbose_name='\u7c7b\u522b\u540d\u79f0')),
                ('reason', models.CharField(blank=True, max_length=40, null=True, verbose_name='\u7533\u8bf7\u539f\u56e0')),
                ('device_status', models.CharField(choices=[('repair', '\u7ef4\u4fee'), ('normal', '\u6b63\u5e38'), ('check', '\u68c0\u67e5')], default='repair', max_length=10, verbose_name='\u8bbe\u5907\u72b6\u6001')),
                ('apply_unit', models.CharField(blank=True, choices=[('G0', 'G0'), ('G8', 'G8'), ('G6', 'G6')], max_length=10, null=True, verbose_name='\u7533\u8bf7\u90e8\u95e8')),
                ('apply_time', models.DateField(auto_now=True, null=True, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('rep_status', models.CharField(choices=[('wait', '\u5f85\u7ef4\u62a4'), ('ok', '\u5df2\u4fee\u590d')], default='wait', max_length=20, verbose_name='\u8bbe\u5907\u72b6\u6001')),
            ],
            options={
                'ordering': ['apply_time'],
                'verbose_name': '\u8bbe\u5907\u7ef4\u4fee\u8bb0\u5f55',
                'verbose_name_plural': '\u8bbe\u5907\u7ef4\u4fee\u8bb0\u5f55',
            },
        ),
    ]
