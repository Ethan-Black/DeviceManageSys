# _*_encoding:utf-8 _*_
import xadmin

from outsource.models import DeviceOutsource


class DeviceOutsourceAdmin(object):
    list_display = ['change_id', 'parts_name', 'spec_model']
    search_fields = ['change_id', 'parts_name', 'spec_model']
    list_filter = ['change_id', 'parts_name', 'spec_model']


xadmin.site.register(DeviceOutsource, DeviceOutsourceAdmin)
