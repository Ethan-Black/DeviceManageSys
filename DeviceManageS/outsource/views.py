from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from outsource.models import DeviceOutsource
# Create your views here.


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
def device_outsource(request):
    all_outsources = DeviceOutsource.objects.all()
    return render(request, 'outsource.html', {'outsources': all_outsources})
