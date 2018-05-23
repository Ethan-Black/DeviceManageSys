# _*_encoding:utf-8 _*_
import logging

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from devices.models import DeviceMessage
from repair.models import DeviceRepair

# Create your views here.

# Get an instance of a logger
logger = logging.getLogger('django')


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
def mb_device_rep_apply(request):
    dev_id = request.GET.get('dev_id', '')
    dev_detail = DeviceMessage.objects.get(device_id=dev_id)
    # categories = DeviceCategory.objects.all()

    return render(request, 'mobile_rep_apply.html', {'dev_detail': dev_detail})


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
def mb_rep_apply(request):
    logger.info('Success to repair apply!')

    # device_id = request.POST.get('device_id')
    apply_id = request.POST.get('apply_id')
    if apply_id:
        device_name = request.POST.get('device_name', '')
        # apply_id = request.POST.get('apply_id', '')
        category = request.POST.get('category', '')
        status = request.POST.get('status', '')
        reason = request.POST.get('reason', '')
        apply_unit = request.POST.get('apply_unit', '')

        dev_rep = DeviceRepair()
        dev_rep.device_name = device_name
        # dev_add.device_id = device_id
        dev_rep.apply_id = apply_id
        dev_rep.category_name = category
        dev_rep.device_status = status
        dev_rep.apply_unit = apply_unit
        dev_rep.reason = reason
        # dev_rep.device_id = device_id
        dev_rep.save()

        DeviceMessage.objects.filter(device_name=device_name).update(device_status=status)

    devices_rep = DeviceRepair.objects.all()

    return render(request, 'mobile_pending.html', {'devices_rep': devices_rep})


@login_required
def mb_get_reps(request):
    logger.info('Check the work order now!')

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
        .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'belong_man')
    return render(request, 'mobile_pending.html', {'devices_rep': devices_rep, 'flag': user_flag})


@login_required
def mb_get_reps_me(request):
    apply_id = request.GET.get('apply_id', '')
    if apply_id:
        DeviceRepair.objects.filter(apply_id=apply_id).update(rep_status='ok')
    # plan_id = request.GET.get('plan_id', '')
    # if plan_id:
    #     DeviceBuyPlan.objects.filter(plan_id=plan_id).update(plan_model='ok')
    user_flag = request.session.get('flag')
    user = request.session.get('username', '-')
    # if user_flag == '0':
    #     devices_plan = DeviceBuyPlan.objects.filter(plan_model='wait')\
    #         .values('plan_id', 'parts_name', 'num', 'plan_time', 'spec_model', 'apply_unit')
    #     devices_rep = DeviceRepair.objects.filter(rep_status='wait')
    #     return render(request, 'mobile_pending.html',
    #                   {'devices_rep': devices_rep, 'devices_plan': devices_plan, 'flag': user_flag})
    # else:
    devices_rep = DeviceRepair.objects.filter(rep_status='wait', belong_man=user)\
        .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'belong_man')
    return render(request, 'mobile_pending_me.html', {'devices_rep': devices_rep, 'flag': user_flag})


def mb_robbing(request):
    apply_id = request.GET.get('apply_id', '')
    user_flag = request.session.get('flag')
    if apply_id:
        man = DeviceRepair.objects.filter(apply_id=apply_id)[0].belong_man
        if man == '-':
            user = request.session.get('username', '-')
            DeviceRepair.objects.filter(apply_id=apply_id).update(belong_man=user)
            devices_rep = DeviceRepair.objects.filter(rep_status='wait', belong_man=user) \
                .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'belong_man')
            return render(request, 'mobile_pending_me.html', {'devices_rep': devices_rep, 'flag': user_flag})
        else:
            devices_rep = DeviceRepair.objects.filter(rep_status='wait') \
                .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'belong_man')
            return render(request, 'mobile_pending.html', {'devices_rep': devices_rep, 'flag': user_flag})

    # devices_rep = DeviceRepair.objects.filter(rep_status='wait', belong_man=user)\
    #     .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'category_name')
    else:
        devices_rep = DeviceRepair.objects.filter(rep_status='wait') \
            .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'belong_man')
        return render(request, 'mobile_pending.html', {'devices_rep': devices_rep, 'flag': user_flag})


def mb_dispatch(request):
    apply_id = request.POST.get('apply_id', '')
    user = request.POST.get('man', '')
    user_flag = request.session.get('flag')
    if apply_id:
        man = DeviceRepair.objects.filter(apply_id=apply_id)[0].belong_man
        if man == '-':
            DeviceRepair.objects.filter(apply_id=apply_id).update(belong_man=user)
    devices_rep = DeviceRepair.objects.filter(rep_status='wait') \
        .values('apply_id', 'apply_unit', 'apply_time', 'device_name', 'rep_status', 'reason', 'belong_man')
    return render(request, 'mobile_pending.html', {'devices_rep': devices_rep, 'flag': user_flag})
