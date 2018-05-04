# _*_encoding:utf-8 _*_
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class GlobalSettings(object):
    site_title = u'设备后台管理系统'
    site_footer = u'设备管理系统'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'add_time']
    search_fields = ['title', 'url', 'image', 'index', 'add_time']
    list_filter = ['title', 'url', 'image', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
