# _*_encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DeviceBuyPlan(models.Model):
    plan_id = models.CharField(max_length=20, verbose_name=u'计划编号', null=True, blank=True)
    parts_name = models.CharField(max_length=30, verbose_name=u'部件名称', null=True, blank=True)
    spec_model = models.CharField(max_length=20, verbose_name=u'规格型号', null=True, blank=True)
    num = models.CharField(max_length=5, verbose_name=u'数量', null=True, blank=True)
    tax_price = models.CharField(max_length=10, verbose_name=u'含税价格', null=True, blank=True)
    tax_rate = models.CharField(max_length=10, verbose_name=u'税率', null=True, blank=True)
    no_tax_price = models.CharField(max_length=10, verbose_name=u'不含税价格', null=True, blank=True)
    remark = models.CharField(max_length=10, verbose_name=u'备注', null=True, blank=True)
    plan_time = models.DateField(verbose_name=u'计划时间', null=True, blank=True, auto_now=True)
    apply_unit = models.CharField(choices=(('G0', u'G0'), ('G8', u'G8'), ('G6', u'G6')),
                                  max_length=10, verbose_name=u'申请部门', null=True, blank=True)
    plan_class = models.CharField(choices=(('购置', u'购置'), ('更新', u'更新'), ('回收', u'回收')),
                                  max_length=20, verbose_name=u'计划类别', null=True, blank=True)
    plan_model = models.CharField(choices=(('审批通过', u'审批通过'), ('审批未通过', u'审批未通过'), ('待审批', u'待审批')),
                                  max_length=20, verbose_name=u'计划状态', null=True, blank=True, default='待审批')
    plan_no = models.CharField(max_length=30, verbose_name=u'未通过原因', null=True, blank=True)

    class Meta:
        verbose_name = u'计划'
        verbose_name_plural = verbose_name
        ordering = ['plan_time']