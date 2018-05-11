# _*_encoding:utf-8 _*_
import base64
import os
import qrcode
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.six import BytesIO, StringIO

from PIL import Image
import xlwt
from xlwt import Workbook

from devices.models import DeviceMessage

# Create your views here.


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
