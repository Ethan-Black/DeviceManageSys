# _*_encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DeviceMessage(models.Model):
    device_id = models.CharField(max_length=20, verbose_name=u'设备编号', null=True, blank=True)
    device_name = models.CharField(max_length=10, verbose_name=u'设备名称')
    category_name = models.CharField(choices=(('lift_dev', u'起重机械'), ('car', u'汽车')),
                                     max_length=30, verbose_name=u'类别名称')
    device_model = models.CharField(max_length=20, verbose_name=u'设备型号', null=True, blank=True)
    im_part_name = models.CharField(max_length=10, verbose_name=u'重要配件名称', null=True, blank=True)
    im_part_num = models.CharField(max_length=10, verbose_name=u'重要配件数', null=True, blank=True)
    device_status = models.CharField(choices=(('repair', u'维修'), ('normal', u'正常'), ('check', u'检查')),
                                     max_length=10, verbose_name=u'设备状态')
    make_unit = models.CharField(max_length=10, verbose_name=u'制造单位', null=True, blank=True)
    make_date = models.DateField(verbose_name=u'制造日期', null=True, blank=True)
    in_date = models.DateField(verbose_name=u'进厂日期', null=True, blank=True)
    use_date = models.DateField(verbose_name=u'开用日期', null=True, blank=True)
    belong_id = models.CharField(choices=(('G0', u'G0'), ('G8', u'G8'), ('G6', u'G6')),
                                 max_length=5, verbose_name=u'所属部门编号')
    employee_id = models.CharField(max_length=20, verbose_name=u'操作工人号', null=True, blank=True)
    repair_per = models.CharField(max_length=20, verbose_name=u'检修周期', null=True, blank=True)
    change_per = models.CharField(max_length=20, verbose_name=u'更换周期', null=True, blank=True)
    ps = models.CharField(max_length=20, verbose_name=u'备注', null=True, blank=True)
    datas = models.CharField(max_length=20, verbose_name=u'相关资料', null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png",
                              max_length=100, verbose_name=u'设备图片', null=True, blank=True)
    contact = models.CharField(max_length=10, verbose_name=u'联系人', null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name=u'联系电话', null=True, blank=True)
    made_id = models.CharField(max_length=20, verbose_name=u'出厂编号', null=True, blank=True)
    place = models.CharField(max_length=20, verbose_name=u'存放地点', null=True, blank=True)
    made_time = models.DateField(verbose_name=u'出厂日期', null=True, blank=True)
    value = models.CharField(max_length=20, verbose_name=u'本币原值')
    last_rep_time = models.DateField(verbose_name=u'上次检修时间', null=True, blank=True)
    next_rep_time = models.DateField(verbose_name=u'下次检修时间', null=True, blank=True)
    device_code = models.CharField(max_length=20, verbose_name=u'设备代码', null=True, blank=True)
    device_spec = models.CharField(max_length=20, verbose_name=u'设备规格', null=True, blank=True)
    resp_per = models.CharField(max_length=10, verbose_name=u'设备负责人', null=True, blank=True)
    device_class = models.CharField(max_length=20, verbose_name=u'设备分类', null=True, blank=True)
    device_cate = models.CharField(max_length=20, verbose_name=u'设备类别', null=True, blank=True)
    tech_cate = models.CharField(max_length=20, verbose_name=u'工艺类别', null=True, blank=True)
    belong_place = models.CharField(max_length=20, verbose_name=u'所属地点', null=True, blank=True)
    supplier = models.CharField(max_length=20, verbose_name=u'供应商', null=True, blank=True)
    device_rank = models.CharField(choices=(('special', u'A特种设备'), ('important', u'B重要设备'), ('normal', u'C一般设备')),
                                   max_length=20, verbose_name=u'设备等级')
    enter = models.CharField(max_length=20, verbose_name=u'录入人', null=True, blank=True)
    enter_time = models.DateField(verbose_name=u'录入时间', null=True, blank=True)
    leader_appr = models.CharField(max_length=20, verbose_name=u'部门领导审批', null=True, blank=True)
    leader_appr_time = models.DateField(verbose_name=u'部门领导审批时间', null=True, blank=True)
    manage_unit = models.CharField(max_length=20, verbose_name=u'管理部门', null=True, blank=True)
    register_code = models.CharField(max_length=20, verbose_name=u'注册代码', null=True, blank=True)
    assets_class = models.CharField(max_length=20, verbose_name=u'资产类别', null=True, blank=True)

    class Meta:
        verbose_name = u'设备信息'
        verbose_name_plural = verbose_name
        ordering = ['enter_time']


class DeviceCategory(models.Model):
    cate_id = models.CharField(max_length=5, verbose_name=u'类别编号')
    cate_name = models.CharField(max_length=30, verbose_name=u'类别名称')
    remark = models.CharField(max_length=30, verbose_name=u'备注', null=True, blank=True)
    complete_status = models.CharField(max_length=10, verbose_name=u'完成情况', null=True, blank=True)

    class Meta:
        verbose_name = u'设备类别'
        verbose_name_plural = verbose_name


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


class DeviceBuyPlan(models.Model):
    plan_id = models.CharField(max_length=20, verbose_name=u'计划编号')
    parts_name = models.CharField(max_length=30, verbose_name=u'部件名称')
    spec_model = models.CharField(max_length=20, verbose_name=u'规格型号', null=True, blank=True)
    num = models.CharField(max_length=5, verbose_name=u'数量')
    tax_price = models.CharField(max_length=10, verbose_name=u'含税价格', null=True, blank=True)
    tax_rate = models.CharField(max_length=10, verbose_name=u'税率', null=True, blank=True)
    no_tax_price = models.CharField(max_length=10, verbose_name=u'不含税价格', null=True, blank=True)
    remark = models.CharField(max_length=10, verbose_name=u'备注', null=True, blank=True)
    plan_time = models.DateField(verbose_name=u'计划时间', null=True, blank=True, auto_now=True)
    apply_unit = models.CharField(choices=(('G0', u'G0'), ('G8', u'G8'), ('G6', u'G6')),
                                  max_length=10, verbose_name=u'申请部门', null=True, blank=True)
    plan_class = models.CharField(choices=(('buy', u'购置'), ('update', u'更新'), ('recycle', u'回收')),
                                  max_length=20, verbose_name=u'计划类别', null=True, blank=True)
    plan_model = models.CharField(choices=(('ok', u'审批通过'), ('no', u'审批未通过'), ('wait', u'待审批')),
                                  max_length=20, verbose_name=u'计划状态', null=True, blank=True, default='wait')
    plan_no = models.CharField(max_length=30, verbose_name=u'未通过原因', null=True, blank=True)

    class Meta:
        verbose_name = u'计划'
        verbose_name_plural = verbose_name
        ordering = ['plan_time']
