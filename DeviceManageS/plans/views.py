# _*_encoding:utf-8 _*_
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from plans.models import DeviceBuyPlan
# Create your views here.


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
    # return JsonResponse(serializers.serialize('json', dev_plan_detail), content_type="application/json", safe=False)
    # else:
    dev_detail = dev_plan_detail[0]
    return render(request, 'mobile_plan_do_msg.html', {'dev_detail': dev_detail, 'flag': user_flag})


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
