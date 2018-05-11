# _*_encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DeviceOutsource(models.Model):
    change_id = models.CharField(max_length=20, verbose_name=u'变更编号')
    parts_name = models.CharField(max_length=30, verbose_name=u'配件名称')
    spec_model = models.CharField(max_length=20, verbose_name=u'规格型号', null=True, blank=True)
    num = models.CharField(max_length=5, verbose_name=u'数量')
    tax_price = models.CharField(max_length=10, verbose_name=u'含税价格', null=True, blank=True)
    tax_rate = models.CharField(max_length=10, verbose_name=u'税率', null=True, blank=True)
    no_tax_price = models.CharField(max_length=10, verbose_name=u'不含税价格', null=True, blank=True)
    remark = models.CharField(max_length=10, verbose_name=u'备注', null=True, blank=True)

    class Meta:
        verbose_name = u'设备委外记录'
        verbose_name_plural = verbose_name
