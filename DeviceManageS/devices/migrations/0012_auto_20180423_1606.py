# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-23 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_auto_20180423_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicerepair',
            name='apply_id',
            field=models.CharField(max_length=20, verbose_name='\u7533\u8bf7\u7f16\u53f7'),
        ),
    ]
