# _*_encoding:utf-8 _*_
import StringIO
import base64
import json

import os
import xlwt
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# import zbar
from PIL import Image
from xlwt import Workbook

from ua_recognization import choose_template
from .models import DeviceMessage, DeviceCategory, DeviceOutsource, DeviceRepair, DeviceBuyPlan

# Create your views here.


@login_required
def mb_index(request):
    return render(request, 'mobile_index.html')


@login_required
@choose_template('list.html')
def device_category(request, template_name=''):
    all_categories = DeviceCategory.objects.values('cate_id', 'cate_name')
    return render(request, template_name, {'categories': all_categories})


@login_required
@choose_template('message.html')
def device_message(request, template_name=''):
    if request.GET.get("dev_id"):
        dev_id = request.GET.get("dev_id")
        cate = DeviceMessage.objects.get(device_id=dev_id).category_name
        DeviceMessage.objects.get(device_id=dev_id).delete()

        if cate:
            devices = DeviceMessage.objects.filter(category_name=cate).values('device_name', 'device_id')
    else:
        cate_dic = {'lift_dev': u'起重机械', 'car': u'汽车'}
        cate_parm = request.GET.get('category', '')
        category = list(cate_dic.keys())[list(cate_dic.values()).index(cate_parm)]
        if category:
            devices = DeviceMessage.objects.filter(category_name=category).values('device_name', 'device_id')

    # devices = None
    # if all_devices:
    #     devices = all_devices[0]

    categories = DeviceCategory.objects.values('cate_name')

    return render(request, template_name, {'devices': devices, 'categories': categories})


@login_required
def device_detail(request):
    dev_id = request.GET.get('dev_id', '')
    user_flag = request.session.get('flag')
    dev_details = DeviceMessage.objects.filter(device_id=dev_id)
    # categories = DeviceCategory.objects.all()

    if request.is_ajax():
        return JsonResponse(serializers.serialize('json', dev_details), content_type="application/json", safe=False)
    else:
        dev_detail = dev_details[0]
        return render(request, 'mobile_dev_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


@login_required
def device_rep_detail(request):
    apply_id = request.GET.get('apply_id', '')
    user_flag = request.session.get('flag')
    dev_rep_details = DeviceRepair.objects.filter(apply_id=apply_id)
    # categories = DeviceCategory.objects.all()

    if request.is_ajax():
        return JsonResponse(serializers.serialize('json', dev_rep_details), content_type="application/json", safe=False)
    else:
        dev_detail = dev_rep_details[0]
        return render(request, 'mobile_rep_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


@login_required
def device_rep_do_detail(request):
    apply_id = request.GET.get('apply_id', '')
    user_flag = request.session.get('flag')
    dev_rep_details = DeviceRepair.objects.filter(apply_id=apply_id)
    # categories = DeviceCategory.objects.all()

    # if request.is_ajax():
    #     return JsonResponse(serializers.serialize('json', dev_rep_details), content_type="application/json", safe=False)
    # else:
    dev_detail = dev_rep_details[0]
    return render(request, 'mobile_rep_do_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


@login_required
def device_edit(request):
    dev_id = request.GET.get('dev_id', '')
    dev_detail = DeviceMessage.objects.filter(device_id=dev_id)[0]
    categories = DeviceCategory.objects.all()

    return render(request, 'edit.html', {'dev_detail': dev_detail, 'categories': categories})


@login_required
def mb_device_edit(request):
    dev_id = request.GET.get('dev_id', '')
    dev_detail = DeviceMessage.objects.get(device_id=dev_id)
    # categories = DeviceCategory.objects.all()

    return render(request, 'mobile_dev_edit.html', {'dev_detail': dev_detail})


@login_required
def mb_device_rep_apply(request):
    dev_id = request.GET.get('dev_id', '')
    dev_detail = DeviceMessage.objects.get(device_id=dev_id)
    # categories = DeviceCategory.objects.all()

    return render(request, 'mobile_rep_apply.html', {'dev_detail': dev_detail})


@login_required
def device_status_details(request):
    status_dic = {'repair', u'维修', 'normal', u'正常', 'check', u'检查'}
    status_parm = request.GET.get('status', '')
    device_sta = list(status_dic.keys())[list(status_dic.values()).index(status_parm)]
    if device_sta:
        dev_sta_detail = DeviceMessage.objects.filter(device_status=device_sta)

    return render(request, 'status_details.html', {'sta_details': dev_sta_detail})


@login_required
def device_outsource(request):
    all_outsources = DeviceOutsource.objects.all()
    return render(request, 'outsource.html', {'outsources': all_outsources})


@login_required
def ajax_dev_del(request):
    if request.method == "GET":
        dev_id = request.GET.get('dev_id')
        if dev_id:
            cate = DeviceMessage.objects.get(device_id=dev_id).category_name
            DeviceMessage.objects.get(device_id=dev_id).delete()

            if cate:
                devices = DeviceMessage.objects.filter(category_name=cate)
                categories = DeviceCategory.objects.all()

            return render(request, 'message.html', {'devices': devices, 'categories': categories})


@login_required
def edit_success(request):
    device_id = request.POST.get('device_id')
    device_name = request.POST.get('device_name')
    device_model = request.POST.get('device_model')
    category = request.POST.get('category')
    status = request.POST.get('status')

    dev = DeviceMessage.objects.get(device_id=device_id)
    if dev.device_name == device_name and dev.device_model == device_model and \
            dev.category_name == category and dev.device_status == status:
        pass
    else:
        dev.device_name = device_name
        dev.device_status = status
        dev.category_name = category
        dev.device_model = device_model
        dev.save()

    dev_detail = dev
    user_flag = request.session.get('flag')
    categories = DeviceCategory.objects.all()
    return render(request, 'details.html', {'dev_detail': dev_detail, 'flag': user_flag, 'categories': categories})


@login_required
def mb_dev_edit_success(request):
    device_id = request.POST.get('device_id')
    device_name = request.POST.get('device_name')
    device_model = request.POST.get('device_model')
    category = request.POST.get('category')
    status = request.POST.get('status')
    image = request.FILES.get('img')

    dev = DeviceMessage.objects.get(device_id=device_id)
    if dev.device_name == device_name and dev.device_model == device_model \
            and dev.category_name == category and dev.device_status == status \
            and dev.image == image:
        pass
    else:
        dev.device_name = device_name
        dev.device_status = status
        dev.category_name = category
        dev.device_model = device_model
        dev.image = image
        dev.save()

    dev_detail = dev
    user_flag = request.session.get('flag')
    # categories = DeviceCategory.objects.all()
    return render(request, 'mobile_dev_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


@login_required
def mb_out_edit_success(request):
    change_id = request.POST.get('change_id')
    parts_name = request.POST.get('parts_name')
    spec_model = request.POST.get('spec_model')
    num = request.POST.get('num')
    tax_price = request.POST.get('tax_price')
    tax_rate = request.POST.get('tax_rate')
    no_tax_price = request.POST.get('no_tax_price')
    remark = request.POST.get('remark')

    dev = DeviceOutsource.objects.get(change_id=change_id)
    if dev.parts_name == parts_name and dev.spec_model == spec_model and \
            dev.num == num and dev.tax_price == tax_price and dev.no_tax_price == no_tax_price \
            and dev.tax_rate == tax_rate:
        pass
    else:
        dev.change_id = change_id
        dev.parts_name = parts_name
        dev.spec_model = spec_model
        dev.tax_price = tax_price
        dev.no_tax_price = no_tax_price
        dev.tax_rate = tax_rate
        dev.remark = remark
        dev.save()

    dev_detail = dev
    user_flag = request.session.get('flag')
    # categories = DeviceCategory.objects.all()
    return render(request, 'mobile_out_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


@login_required
def dev_rep_apply(request):
    dev_id = request.GET.get('dev_id', '')
    if dev_id:
        dev_detail = DeviceMessage.objects.get(device_id=dev_id)
        return render(request, 'repair_apply.html', {'dev_detail': dev_detail})
    else:
        dev_detail = {'': ''}
        return render(request, 'repair_apply.html', {'dev_detail': dev_detail})


@login_required
def dev_repair(request):
    if request.method == 'POST':
        device_id = request.POST.get('device_id', '')
        device_name = request.POST.get('device_name', '')
        apply_id = request.POST.get('apply_id', '')
        reason = request.POST.get('reason', '')
        apply_unit = request.POST.get('apply_unit', '')
        status = request.POST.get('status', '')

        dev_rep = DeviceRepair()
        dev_rep.device_name = device_name
        dev_rep.device_id = device_id
        dev_rep.apply_id = apply_id
        dev_rep.apply_unit = apply_unit
        dev_rep.reason = reason
        dev_rep.device_status = status
        dev_rep.save()

        return render(request, 'repair.html', {'dev_rep': dev_rep})

    elif request.method == 'GET':
        dev_rep = DeviceRepair.objects.all()[0]

        return render(request, 'repair.html', {'dev_rep': dev_rep})


@login_required
def device_normal(request):
    status = request.GET.get('status')
    all_devices = DeviceMessage.objects.filter(device_status=status)
    return render(request, 'message.html', {'all_devices': all_devices})


@login_required
def device_add(request):
    # device_id = request.POST.get('device_id')
    device_name = request.POST.get('device_name', '')
    device_model = request.POST.get('device_model', '')
    category = request.POST.get('category', '')
    status = request.POST.get('status', '')
    value = request.POST.get('value', '')
    device_id = request.POST.get('device_id', '')
    # add_time = request.POST.get('add_time', '')

    dev_add = DeviceMessage()
    dev_add.device_name = device_name
    # dev_add.device_id = device_id
    dev_add.device_model = device_model
    dev_add.category_name = category
    dev_add.device_status = status
    # dev_add.enter_time = add_time
    dev_add.value = value
    dev_add.device_id = device_id
    dev_add.save()

    devices = DeviceMessage.objects.filter(category_name=category)

    return render(request, 'mobile_message.html', {'devices': devices})


@login_required
def mobile_dev_cate(request):
    if request.is_ajax():
        all_categories = DeviceCategory.objects.all()
        return JsonResponse(serializers.serialize('json', all_categories), content_type="application/json", safe=False)


@login_required
def mobile_del(request):
    dev_id = request.GET.get('dev_id')
    dev = DeviceMessage.objects.get(device_id=dev_id)
    category = dev.category_name
    dev.delete()
    devices = DeviceMessage.objects.filter(category_name=category)

    return render(request, 'mobile_message.html', {'devices': devices})


@login_required
def mb_rep_apply(request):
    # device_id = request.POST.get('device_id')
    device_name = request.POST.get('device_name', '')
    apply_id = request.POST.get('apply_id', '')
    category = request.POST.get('category', '')
    status = request.POST.get('status', '')
    reason = request.POST.get('reason', '')
    device_id = request.POST.get('device_id', '')
    apply_unit = request.POST.get('apply_unit', '')

    dev_rep = DeviceRepair()
    dev_rep.device_name = device_name
    # dev_add.device_id = device_id
    dev_rep.apply_id = apply_id
    dev_rep.category_name = category
    dev_rep.device_status = status
    dev_rep.apply_unit = apply_unit
    dev_rep.reason = reason
    dev_rep.device_id = device_id
    dev_rep.save()

    devices_rep = DeviceRepair.objects.all()

    return render(request, 'mobile_pending.html', {'devices_rep': devices_rep})


@login_required
def mb_get_reps(request):
    apply_id = request.GET.get('apply_id', '')
    if apply_id:
        DeviceRepair.objects.filter(apply_id=apply_id).update(rep_status='ok')
    # plan_id = request.GET.get('plan_id', '')
    # if plan_id:
    #     DeviceBuyPlan.objects.filter(plan_id=plan_id).update(plan_model='ok')
    user_flag = request.session.get('flag')
    # if user_flag == '0':
    #     devices_plan = DeviceBuyPlan.objects.filter(plan_model='wait')\
    #         .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    #     devices_rep = DeviceRepair.objects.filter(rep_status='wait')
    #     return render(request, 'mobile_pending.html',
    #                   {'devices_rep': devices_rep, 'devices_plan': devices_plan, 'flag': user_flag})
    # else:
    devices_rep = DeviceRepair.objects.filter(rep_status='wait')\
        .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'category_name')
    return render(request, 'mobile_pending.html', {'devices_rep': devices_rep, 'flag': user_flag})


@login_required
def mb_pending_plan(request):
    # apply_id = request.GET.get('apply_id', '')
    # if apply_id:
    #     DeviceRepair.objects.filter(apply_id=apply_id).update(rep_status='ok')
    plan_id = request.GET.get('plan_id', '')
    if plan_id:
        DeviceBuyPlan.objects.filter(plan_id=plan_id).update(plan_model='ok')
    user_flag = request.session.get('flag')
    # if user_flag == '0':
    devices_plan = DeviceBuyPlan.objects.filter(plan_model='wait')\
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    # devices_rep = DeviceRepair.objects.filter(rep_status='wait')
    return render(request, 'mobile_pending_plan.html',
                  {'devices_plan': devices_plan, 'flag': user_flag})


@login_required
def mb_pending_plan_no(request):
    # apply_id = request.GET.get('apply_id', '')
    # if apply_id:
    #     DeviceRepair.objects.filter(apply_id=apply_id).update(rep_status='ok')
    plan_id = request.POST.get('plan_id', '')
    advice = request.POST.get('advice', '')
    if plan_id and advice:
        DeviceBuyPlan.objects.filter(plan_id=plan_id).update(plan_model='no')
        DeviceBuyPlan.objects.filter(plan_id=plan_id).update(plan_no=advice)
    user_flag = request.session.get('flag')
    # if user_flag == '0':
    devices_plan = DeviceBuyPlan.objects.filter(plan_model='wait')\
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    # devices_rep = DeviceRepair.objects.filter(rep_status='wait')
    return render(request, 'mobile_pending_plan.html',
                  {'devices_plan': devices_plan, 'flag': user_flag})


@login_required
def mb_outs(request):
    if request.GET.get("change_id"):
        ch_id = request.GET.get("change_id")
        DeviceOutsource.objects.get(change_id=ch_id).delete()
    all_outs = DeviceOutsource.objects.values('change_id', 'parts_name', 'num')
    return render(request, 'mobile_outsource.html', {'outs': all_outs})


@login_required
def device_out_detail(request):
    change_id = request.GET.get('change_id', '')
    user_flag = request.session.get('flag')
    dev_out_details = DeviceOutsource.objects.filter(change_id=change_id)
    # categories = DeviceCategory.objects.all()

    if request.is_ajax():
        return JsonResponse(serializers.serialize('json', dev_out_details), content_type="application/json", safe=False)
    else:
        dev_detail = dev_out_details[0]
        return render(request, 'mobile_out_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


@login_required
def mb_out_edit(request):
    change_id = request.GET.get('change_id', '')
    out_detail = DeviceOutsource.objects.get(change_id=change_id)
    # categories = DeviceCategory.objects.all()

    return render(request, 'mobile_out_edit.html', {'dev_detail': out_detail})


@login_required
def mb_get_plans(request):
    # plan_id = request.GET.get('plan_id', '')
    # if plan_id:
    #     DeviceRepair.objects.filter(plan_id=plan_id).delete()
    devices_buy_plan = DeviceBuyPlan.objects.filter(plan_model='wait').filter(plan_class='buy')\
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    devices_update_plan = DeviceBuyPlan.objects.filter(plan_model='wait').filter(plan_class='update') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    devices_recycle_plan = DeviceBuyPlan.objects.filter(plan_model='wait').filter(plan_class='recycle') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    return render(request, 'mobile_plan.html', {
        'devices_buy_plan': devices_buy_plan,
        'devices_update_plan': devices_update_plan,
        'devices_recycle_plan': devices_recycle_plan
    })


@login_required
def mb_get_plans_ok(request):
    devices_buy_plan = DeviceBuyPlan.objects.filter(plan_model='ok').filter(plan_class='buy') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    devices_update_plan = DeviceBuyPlan.objects.filter(plan_model='ok').filter(plan_class='update') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    devices_recycle_plan = DeviceBuyPlan.objects.filter(plan_model='ok').filter(plan_class='recycle') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    return render(request, 'mobile_plan_ok.html', {
        'devices_buy_plan': devices_buy_plan,
        'devices_update_plan': devices_update_plan,
        'devices_recycle_plan': devices_recycle_plan
    })


@login_required
def mb_get_plans_no(request):
    devices_buy_plan = DeviceBuyPlan.objects.filter(plan_model='no').filter(plan_class='buy') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    devices_update_plan = DeviceBuyPlan.objects.filter(plan_model='no').filter(plan_class='update') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    devices_recycle_plan = DeviceBuyPlan.objects.filter(plan_model='no').filter(plan_class='recycle') \
        .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    return render(request, 'mobile_plan_no.html', {
        'devices_buy_plan': devices_buy_plan,
        'devices_update_plan': devices_update_plan,
        'devices_recycle_plan': devices_recycle_plan
    })


@login_required
def mb_get_rep_record(request):
    rep_records = DeviceRepair.objects.filter(rep_status='wait')\
        .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason')
    return render(request, 'mobile_rep_record.html', {'rep_records': rep_records})


@login_required
def mb_get_rep_record_ok(request):
    rep_records = DeviceRepair.objects.filter(rep_status='ok')\
        .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason')
    return render(request, 'mobile_rep_record_ok.html', {'rep_records': rep_records})


@login_required
def mb_plan_apply(request):
    # device_id = request.POST.get('device_id')
    parts_name = request.POST.get('parts_name', '')
    plan_id = request.POST.get('plan_id', '')
    num = request.POST.get('num', '')
    spec_model = request.POST.get('spec_model', '')
    plan_class = request.POST.get('plan_class', '')
    remark = request.POST.get('remark', '')
    apply_unit = request.POST.get('apply_unit', '')

    dev_plan = DeviceBuyPlan()
    dev_plan.parts_name = parts_name
    # dev_add.device_id = device_id
    dev_plan.plan_id = plan_id
    dev_plan.num = num
    dev_plan.spec_model = spec_model
    dev_plan.apply_unit = apply_unit
    dev_plan.plan_class = plan_class
    dev_plan.remark = remark
    dev_plan.save()

    devices_plan = DeviceBuyPlan.objects.all()

    return render(request, 'mobile_plan.html', {'devices_plan': devices_plan})


@login_required
def device_plan_detail(request):
    plan_id = request.GET.get('plan_id', '')
    user_flag = request.session.get('flag')
    dev_plan_detail = DeviceBuyPlan.objects.filter(plan_id=plan_id)
    # categories = DeviceCategory.objects.all()

    if request.is_ajax():
        return JsonResponse(serializers.serialize('json', dev_plan_detail), content_type="application/json", safe=False)
    else:
        dev_detail = dev_plan_detail[0]
        return render(request, 'mobile_plan_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


@login_required
def device_plan_do_detail(request):
    plan_id = request.GET.get('plan_id', '')
    user_flag = request.session.get('flag')
    dev_plan_detail = DeviceBuyPlan.objects.filter(plan_id=plan_id)
    # categories = DeviceCategory.objects.all()

    # if request.is_ajax():
    #     return JsonResponse(serializers.serialize('json', dev_plan_detail), content_type="application/json", safe=False)
    # else:
    dev_detail = dev_plan_detail[0]
    return render(request, 'mobile_plan_do_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})



@login_required
def device_plan_agree(request):
    plan_id = request.GET.get('plan_id', '')
    # user_flag = request.session.get('flag')
    dev_detail = DeviceBuyPlan.objects.get(plan_id=plan_id)
    dev_detail.plan_model = 'ok'
    dev_detail.save()
    # categories = DeviceCategory.objects.all()

    # if request.is_ajax():
    #     return JsonResponse(serializers.serialize('json', dev_plan_detail), content_type="application/json", safe=False)
    # else:
    # dev_detail = dev_plan_detail[0]
    return render(request, 'mobile_plan_msg.html', {'dev_detail': dev_detail})


@login_required
def mb_all_devs(request):
    all_lift_devs = DeviceMessage.objects.filter(category_name='lift_dev').values('device_id', 'device_name')
    all_car_devs = DeviceMessage.objects.filter(category_name='car').values('device_id', 'device_name')
    return render(request, 'mobile_dev_query.html', {'all_lift_devs': all_lift_devs, 'all_car_devs': all_car_devs})


@login_required
def mb_excel(request):
    # response = HttpResponse(mimetype='application/vnd.ms-excel')
    # response['Content-Disposition'] = 'attachment;filename=export_dev_msg.xls'
    # wb = xlwt.Workbook(encoding='utf-8')
    # sheet = wb.add_sheet(u'设备信息列表')
    # # 1st line
    # sheet.write(0, 0, '设备编号')
    # sheet.write(0, 1, '设备名称')
    # sheet.write(0, 2, '类别名称')
    # sheet.write(0, 3, '设备型号')
    #
    # row = 1
    # for dev in DeviceMessage.objects.all():
    #     sheet.write(row, 0, dev.device_id)
    #     sheet.write(row, 1, dev.device_name)
    #     sheet.write(row, 2, dev.category_name)
    #     sheet.write(row, 3, dev.device_model)
    #     row = row + 1
    #
    # output = StringIO.StringIO()
    # wb.save(output)
    # output.seek(0)
    # response.write(output.getvalue())
    # return response

    list_obj = DeviceMessage.objects.all()
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"设备信息列表")
        w.write(0, 0, u"设备编号")
        w.write(0, 1, u"设备名称")
        w.write(0, 2, u"类别名称")
        w.write(0, 3, u"设备型号")
        # w.write(0, 4, u"来源")
        # 写入数据
        excel_row = 1
        for obj in list_obj:
            data_id = obj.device_id
            data_user = obj.device_name
            data_time = obj.category_name
            data_content = obj.device_model
            # dada_source = obj.source
            w.write(excel_row, 0, data_id)
            w.write(excel_row, 1, data_user)
            w.write(excel_row, 2, data_time)
            w.write(excel_row, 3, data_content)
            # w.write(excel_row, 4, dada_source)
            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        exist_file = os.path.exists("test.xls")
        if exist_file:
            os.remove(r"test.xls")
        ws.save("test.xls")
        ############################
        sio = StringIO.StringIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test.xls'
        response.write(sio.getvalue())
        return response


@login_required
def mb_qcode(request):
    img_data = request.POST.get('img')
    # scanner = zbar.ImageScanner()
    # print(type(img_data))

    img_d = base64.b64decode(img_data)
    # print(type(img_d))

    # img_file = open('imgtest.jpg', 'wb')
    # img_file.write(img_d)
    # img_file.close()

    return JsonResponse({'1': '1'})

