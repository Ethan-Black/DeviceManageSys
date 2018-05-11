# _*_encoding:utf-8 _*_
import xadmin

from .models import DeviceBuyPlan


class DeviceBuyPlanAdmin(object):
    list_display = ['plan_id', 'parts_name', 'spec_model']
    search_fields = ['plan_id', 'parts_name', 'spec_model']
    list_filter = ['plan_id', 'parts_name', 'spec_model']


xadmin.site.register(DeviceBuyPlan, DeviceBuyPlanAdmin)
