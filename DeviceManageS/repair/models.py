# _*_encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DeviceRepair(models.Model):
    apply_id = models.CharField(max_length=20, verbose_name=u'申请编号', null=True, blank=True)
    device_id = models.CharField(max_length=20, verbose_name=u'设备编号', null=True, blank=True)
    device_name = models.CharField(max_length=10, verbose_name=u'设备名称', null=True, blank=True)
    category_name = models.CharField(choices=(('起重机械', u'起重机械'), ('汽车', u'汽车'), ('金属切削机', u'金属切削机'),
                                              ('铸造及热处', u'铸造及热处'), ('动力设备', u'动力设备'), ('办公用具', u'办公用具')),
                                     max_length=30, verbose_name=u'类别名称', default='汽车')
    reason = models.CharField(max_length=40, verbose_name=u'申请原因', null=True, blank=True)
    device_status = models.CharField(choices=(('维修', u'维修'), ('正常', u'正常'), ('检查', u'检查')),
                                     max_length=10, verbose_name=u'设备状态', default='维修')
    apply_unit = models.CharField(choices=(('G0', u'G0'), ('G8', u'G8'), ('G6', u'G6')),
                                  max_length=10, verbose_name=u'申请部门', null=True, blank=True)
    apply_time = models.DateField(verbose_name=u'申请时间', null=True, blank=True, auto_now=True)
    rep_status = models.CharField(choices=(('待维护', u'待维护'), ('已修复', u'已修复')),
                                  max_length=20, verbose_name=u'设备状态', default='待维护')
    belong_man = models.CharField(choices=(('liu', u'liu'), ('-', u'-')),
                                  max_length=20, verbose_name=u'负责人', default='-')

    class Meta:
        verbose_name = u'设备维修记录'
        verbose_name_plural = verbose_name
        ordering = ['apply_time']
