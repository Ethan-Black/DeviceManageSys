# _*_encoding:utf-8 _*_
import xadmin
from xadmin import views

from .models import DeviceMessage, DeviceCategory, DeviceOutsource, DeviceRepair, DeviceBuyPlan


class DeviceMessageAdmin(object):
    list_display = ['device_id', 'device_name', 'category_name', 'device_model']
    search_fields = ['device_id', 'device_name', 'category_name', 'device_model']
    list_filter = ['device_id', 'device_name', 'category_name', 'device_model']


class DeviceCategoryAdmin(object):
    list_display = ['cate_id', 'cate_name', 'remark', 'complete_status']
    search_fields = ['cate_id', 'cate_name', 'remark', 'complete_status']
    list_filter = ['cate_id', 'cate_name', 'remark', 'complete_status']


class DeviceOutsourceAdmin(object):
    list_display = ['change_id', 'parts_name', 'spec_model']
    search_fields = ['change_id', 'parts_name', 'spec_model']
    list_filter = ['change_id', 'parts_name', 'spec_model']


class DeviceRepairAdmin(object):
    list_display = ['device_id', 'device_name', 'device_status', 'apply_id']
    search_fields = ['device_id', 'device_name', 'device_status', 'apply_id']
    list_filter = ['device_id', 'device_name', 'device_status', 'apply_id']


class DeviceBuyPlanAdmin(object):
    list_display = ['plan_id', 'parts_name', 'spec_model']
    search_fields = ['plan_id', 'parts_name', 'spec_model']
    list_filter = ['plan_id', 'parts_name', 'spec_model']


xadmin.site.register(DeviceMessage, DeviceMessageAdmin)
xadmin.site.register(DeviceCategory, DeviceCategoryAdmin)
xadmin.site.register(DeviceOutsource, DeviceOutsourceAdmin)
xadmin.site.register(DeviceRepair, DeviceRepairAdmin)
xadmin.site.register(DeviceBuyPlan, DeviceBuyPlanAdmin)
