# _*_encoding:utf-8 _*_
import xadmin

from .models import DeviceRepair


class DeviceRepairAdmin(object):
    list_display = ['device_id', 'device_name', 'device_status', 'apply_id']
    search_fields = ['device_id', 'device_name', 'device_status', 'apply_id']
    list_filter = ['device_id', 'device_name', 'device_status', 'apply_id']


xadmin.site.register(DeviceRepair, DeviceRepairAdmin)
