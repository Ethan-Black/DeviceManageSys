# _*_encoding:utf-8 _*_
import xadmin
from xadmin import views

from .models import DeviceMessage, DeviceCategory


class DeviceMessageAdmin(object):
    list_display = ['device_id', 'device_name', 'category_name', 'device_model']
    search_fields = ['device_id', 'device_name', 'category_name', 'device_model']
    list_filter = ['device_id', 'device_name', 'category_name', 'device_model']


class DeviceCategoryAdmin(object):
    list_display = ['cate_id', 'cate_name', 'remark', 'complete_status']
    search_fields = ['cate_id', 'cate_name', 'remark', 'complete_status']
    list_filter = ['cate_id', 'cate_name', 'remark', 'complete_status']


xadmin.site.register(DeviceMessage, DeviceMessageAdmin)
xadmin.site.register(DeviceCategory, DeviceCategoryAdmin)


# xadmin.site.register(DeviceBuyPlan, DeviceBuyPlanAdmin)
