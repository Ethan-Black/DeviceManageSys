"""DeviceManageS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

import xadmin
from django.views.static import serve

from DeviceManageS.settings import MEDIA_ROOT
from outsource.views import mb_outs, device_out_detail, mb_out_edit, mb_out_edit_success
from plans.views import mb_pending_plan, mb_get_plans, mb_get_plans_ok, mb_plan_apply, device_plan_detail, \
    device_plan_do_detail, mb_pending_plan_no, mb_get_plans_no
from repair.views import dev_repair, mb_rep_apply, mb_get_reps, mb_get_rep_record, mb_get_rep_record_ok, \
    mb_device_rep_apply, device_rep_detail, device_rep_do_detail
from tools.views import generate_qrcode, mb_excel, mb_qcode
from users.views import LoginView, MobileLoginView, mb_userinfo, user_logout, mb_userinfo_edit, mb_me_edit_success
from devices.views import device_message, device_detail, device_category, \
    device_status_details, device_edit, ajax_dev_del, edit_success, \
    dev_rep_apply, device_add, mobile_dev_cate, mobile_del, mb_device_edit, mb_dev_edit_success, mb_all_devs, mb_index

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^index/$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^list/$', device_category, name='list'),
    url('^check/$', TemplateView.as_view(template_name='check.html'), name='check'),
    url('^repair/$', dev_repair, name='repair'),
    url('^repair_apply/$', dev_rep_apply, name='repair_apply'),
    url('^details/$', device_detail, name='details'),
    url('^message/$', device_message, name='message'),
    url('^status/$', TemplateView.as_view(template_name='status.html'), name='status'),
    url('^status_details/$', device_status_details, name='status_details'),
    url('^outsource/$', TemplateView.as_view(template_name='outsource.html'), name='outsource'),
    url('^edit/$', device_edit, name='edit'),
    url(r'^details/delete/', ajax_dev_del, name='ajax_dev_del'),
    url(r'^edit/success/', edit_success, name='edit_success'),

    url('^mobile_list/$', device_category, name='mobile_list'),
    url('^mobile_message/$', device_message, name='mobile_message'),
    url('^mobile_index/$', mb_index, name='mobile_index'),
    url('^mobile_dev_query/$', mb_all_devs, name='mobile_dev_query'),
    url('^mobile_excel/$', mb_excel, name='mobile_excel'),
    url('^mobile_qrcode/$', generate_qrcode, name='mobile_qrcode'),

    url('^mobile_login/$', MobileLoginView.as_view(), name='mobile_login'),
    url('^mobile_logout/$', user_logout, name='mobile_logout'),

    # url('^mobile_index/$', TemplateView.as_view(template_name='mobile_index.html'), name='mobile_index'),
    url(r'^mobile_add/success/', device_add, name='mobile_add_success'),
    url(r'^mobile_get_list/', mobile_dev_cate, name='mobile_get_list'),
    # url(r'^mobile_get_details/', device_detail, name='mobile_get_details'),
    url(r'^mobile_rep_apply/success/', mb_rep_apply, name='mobile_rep_apply_success'),

    url(r'^mobile_pending_plan/$', mb_pending_plan, name='mobile_pending_plan'),
    url(r'^mobile_pending/$', mb_get_reps, name='mobile_pending'),

    url(r'^mobile_plan/', mb_get_plans, name='mobile_plan'),
    url(r'^mobile_plan_ok/', mb_get_plans_ok, name='mobile_plan_ok'),
    url(r'^mobile_plan_no/', mb_get_plans_no, name='mobile_plan_no'),
    url(r'^mobile_plan_apply/', mb_plan_apply, name='mobile_plan_apply'),
    url(r'^mobile_get_plan_details/', device_plan_detail, name='mobile_get_rep_details'),
    url(r'^mobile_plan_msg/', device_plan_detail, name='mobile_plan_msg'),
    url(r'^mobile_plan_do_msg/', device_plan_do_detail, name='mobile_plan_do_msg'),
    url(r'^mobile_plan_do_no/', mb_pending_plan_no, name='mobile_plan_do_no'),

    url(r'^mobile_rep_record/$', mb_get_rep_record, name='mobile_rep_record'),
    url(r'^mobile_rep_record_ok/$', mb_get_rep_record_ok, name='mobile_rep_record_ok'),
    url(r'^mobile_rep_apply/', mb_device_rep_apply, name='mobile_rep_apply'),
    url(r'^mobile_rep_msg/', device_rep_detail, name='mobile_rep_msg'),
    url(r'^mobile_rep_do_msg/', device_rep_do_detail, name='mobile_rep_do_msg'),
    url(r'^mobile_get_rep_details/', device_rep_detail, name='mobile_get_rep_details'),

    url(r'^mobile_dev_msg/', device_detail, name='mobile_dev_msg'),
    url('^mobile_dev_edit/$', mb_device_edit, name='mobile_dev_edit'),
    url(r'^mobile_dev_edit/success/', mb_dev_edit_success, name='mobile_dev_edit_success'),
    url(r'^mobile_dev_del/', mobile_del, name='mobile_add_success'),

    url('^mobile_outsource/$', mb_outs, name='mobile_outsource'),
    url(r'^mobile_out_msg/', device_out_detail, name='mobile_out_msg'),
    url('^mobile_out_edit/$', mb_out_edit, name='mobile_out_edit'),
    url(r'^mobile_out_edit/success/', mb_out_edit_success, name='mobile_out_edit_success'),
    url(r'^mobile_get_out_details/', device_out_detail, name='mobile_get_out_details'),

    # url(r'^mobile_plan_agree/', device_plan_agree, name='mobile_plan_agree'),

    url('^mobile_me_edit/$', mb_userinfo_edit, name='mobile_me_edit'),
    url('^mobile_me/$', mb_userinfo, name='mobile_me'),
    url(r'^mobile_me_edit/success/', mb_me_edit_success, name='mobile_me_edit_success'),

    url('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),




    url(r'^mobile_qcode/', TemplateView.as_view(template_name='mobile_qcode.html'), name='mobile_qcode'),
    url('^mobile_add/$', mb_qcode, name='mobile_add'),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
