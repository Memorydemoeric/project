from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from common.DataProcess.excel_loads import load_cust_info
from information.models import CustomerInfo


def info_manage(request):
    data = {}
    return render(request, 'info_manage.html', data)


# 批量导入客户信息
def input_cust_info(quest):
    data_lt = []
    path = '/home/fish/Desktop/test/cust_info.xls'
    data = load_cust_info(path, 0)
    tup_field = ('cust_local', 'cust_name', 'cust_mobile_phone', 'cust_address', 'cust_phone_number')
    for foo in data:
        dict_zip = dict(zip(tup_field, foo))
        obj = CustomerInfo(**dict_zip)
        data_lt.append(obj)
    CustomerInfo.objects.bulk_create(data_lt)
    return HttpResponse('客户信息导入成功')