# _*_encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DeviceRepair(models.Model):
    apply_id = models.CharField(max_length=20, verbose_name=u'申请编号')
    device_id = models.CharField(max_length=20, verbose_name=u'设备编号')
    device_name = models.CharField(max_length=10, verbose_name=u'设备名称')
    category_name = models.CharField(choices=(('lift_dev', u'起重机械'), ('car', u'汽车')),
                                     max_length=30, verbose_name=u'类别名称', default='car')
    reason = models.CharField(max_length=40, verbose_name=u'申请原因', null=True, blank=True)
    device_status = models.CharField(choices=(('repair', u'维修'), ('normal', u'正常'), ('check', u'检查')),
                                     max_length=10, verbose_name=u'设备状态', default='repair')
    apply_unit = models.CharField(choices=(('G0', u'G0'), ('G8', u'G8'), ('G6', u'G6')),
                                  max_length=10, verbose_name=u'申请部门', null=True, blank=True)
    apply_time = models.DateField(verbose_name=u'申请时间', null=True, blank=True, auto_now=True)
    rep_status = models.CharField(choices=(('wait', u'待维护'), ('ok', u'已修复')),
                                  max_length=20, verbose_name=u'设备状态', default='wait')

    class Meta:
        verbose_name = u'设备维修记录'
        verbose_name_plural = verbose_name
        ordering = ['apply_time']
