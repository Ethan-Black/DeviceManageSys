# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-03 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=20, verbose_name='\u8bbe\u5907\u7f16\u53f7')),
                ('device_name', models.CharField(max_length=10, verbose_name='\u8bbe\u5907\u540d\u79f0')),
                ('category_name', models.CharField(choices=[('lift_machine', '\u8d77\u91cd\u673a\u68b0'), ('car', '\u6c7d\u8f66')], max_length=10, verbose_name='\u7c7b\u522b\u540d\u79f0')),
                ('device_model', models.CharField(max_length=20, verbose_name='\u8bbe\u5907\u578b\u53f7')),
                ('im_part_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u91cd\u8981\u914d\u4ef6\u540d\u79f0')),
                ('im_part_num', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u91cd\u8981\u914d\u4ef6\u6570')),
                ('device_status', models.CharField(choices=[('repair', '\u7ef4\u4fee'), ('normal', '\u6b63\u5e38'), ('check', '\u68c0\u67e5')], max_length=10, verbose_name='\u8bbe\u5907\u72b6\u6001')),
                ('make_unit', models.CharField(max_length=10, verbose_name='\u5236\u9020\u5355\u4f4d')),
                ('make_date', models.DateField(blank=True, null=True, verbose_name='\u5236\u9020\u65e5\u671f')),
                ('in_date', models.DateField(blank=True, null=True, verbose_name='\u8fdb\u5382\u65e5\u671f')),
                ('use_date', models.DateField(blank=True, null=True, verbose_name='\u5f00\u7528\u65e5\u671f')),
                ('belong_id', models.CharField(choices=[('G0', 'G0'), ('G8', 'G8')], max_length=5, verbose_name='\u6240\u5c5e\u90e8\u95e8\u7f16\u53f7')),
                ('employee_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u64cd\u4f5c\u5de5\u4eba\u53f7')),
                ('repair_per', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u68c0\u4fee\u5468\u671f')),
                ('change_per', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u66f4\u6362\u5468\u671f')),
                ('ps', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5907\u6ce8')),
                ('datas', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u76f8\u5173\u8d44\u6599')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u8bbe\u5907\u56fe\u7247')),
                ('contact', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('made_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u51fa\u5382\u7f16\u53f7')),
                ('place', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5b58\u653e\u5730\u70b9')),
                ('made_time', models.DateField(blank=True, null=True, verbose_name='\u51fa\u5382\u65e5\u671f')),
                ('value', models.CharField(max_length=20, verbose_name='\u672c\u5e01\u539f\u503c')),
                ('last_rep_time', models.DateField(blank=True, null=True, verbose_name='\u4e0a\u6b21\u68c0\u4fee\u65f6\u95f4')),
                ('next_rep_time', models.DateField(blank=True, null=True, verbose_name='\u4e0b\u6b21\u68c0\u4fee\u65f6\u95f4')),
                ('device_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bbe\u5907\u4ee3\u7801')),
                ('device_spec', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bbe\u5907\u89c4\u683c')),
                ('resp_per', models.CharField(max_length=10, verbose_name='\u8bbe\u5907\u8d1f\u8d23\u4eba')),
                ('device_class', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bbe\u5907\u5206\u7c7b')),
                ('device_cate', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bbe\u5907\u7c7b\u522b')),
                ('tech_cate', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5de5\u827a\u7c7b\u522b')),
                ('belong_place', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u6240\u5c5e\u5730\u70b9')),
                ('supplier', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u4f9b\u5e94\u5546')),
                ('device_rank', models.CharField(choices=[('special', 'A\u7279\u79cd\u8bbe\u5907'), ('important', 'B\u91cd\u8981\u8bbe\u5907'), ('normal', 'C\u4e00\u822c\u8bbe\u5907')], max_length=20, verbose_name='\u8bbe\u5907\u7b49\u7ea7')),
                ('enter', models.CharField(max_length=20, verbose_name='\u5f55\u5165\u4eba')),
                ('enter_time', models.DateField(verbose_name='\u5f55\u5165\u65f6\u95f4')),
                ('leader_appr', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u90e8\u95e8\u9886\u5bfc\u5ba1\u6279')),
                ('leader_appr_time', models.DateField(blank=True, null=True, verbose_name='\u90e8\u95e8\u9886\u5bfc\u5ba1\u6279\u65f6\u95f4')),
                ('manage_unit', models.CharField(max_length=20, verbose_name='\u7ba1\u7406\u90e8\u95e8')),
                ('register_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u6ce8\u518c\u4ee3\u7801')),
                ('assets_class', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8d44\u4ea7\u7c7b\u522b')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u4fe1\u606f',
                'verbose_name_plural': '\u8bbe\u5907\u4fe1\u606f',
            },
        ),
    ]
