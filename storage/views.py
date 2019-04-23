from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from common.DataProcess.excel_loads import load_storage_excel
from information.models import CustomerInfo
from storage.models import StorageProduct, StorageHalfFinished


def storage_manage(request):
    data = {}
    return render(request, 'storage_manage.html', data)


def input_pro_info(request):
    data_list = []
    path = '/home/fish/Desktop/test/12.xls'
    data = load_storage_excel(path, 0)
    tup_field = ('pro_type', 'pro_id', 'pro_count', 'pro_cost_unit_price', 'pro_sell_unit_price', 'pro_sell_price')
    for foo in data:
        dict_zip = dict(zip(tup_field, foo))
        obj = StorageProduct(**dict_zip)
        data_list.append(obj)
    StorageProduct.objects.bulk_create(data_list)
    return HttpResponse('成品导入成功')


def input_half_pro_info(request):
    data_list = []
    path = '/home/fish/Desktop/test/11.xls'
    data = load_storage_excel(path, 0)
    tup_field = ('half_type', 'half_id', 'half_count', 'half_cost_unit_price', 'half_sell_unit_price', 'half_sell_price')
    for foo in data:
        dict_zip = dict(zip(tup_field, foo))
        obj = StorageHalfFinished(**dict_zip)
        data_list.append(obj)
    StorageHalfFinished.objects.bulk_create(data_list)
    return HttpResponse('半成品导入成功')