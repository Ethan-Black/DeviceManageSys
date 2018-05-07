# _*_encoding:utf-8 _*_
import qrcode
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.six import BytesIO

from devices.models import DeviceMessage


def generate_qrcode(request):
    dev_id = request.GET.get('dev_id')
    dev = DeviceMessage.objects.get(device_id=dev_id)
    data = u'设备编号：' + dev.device_id + '\n' + u'设备名称：' + dev.device_name
    # data = '123'
    img = qrcode.make(data)

    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    return response
