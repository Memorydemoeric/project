from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from common.DataProcess import file_manage
from common.DataProcess.database_input import purchase_detail_input
from common.DataProcess.excel_loads import load_purchase_detail
from information.models import CustomerInfo, UserInfo
from purchase.forms import PurchaseOrderFroms
from purchase.models import Purchase, PurchaseDetail


def purchase_manage(request):
    data = {}
    return render(request, 'purchase_manage.html', data)


def show_purchase_order(request):
    data = {'title': '创建采购订单'}
    info_lt = []
    usr_lt = []
    if request.method == 'GET':
        cust_info = CustomerInfo.objects.all()
        for info in cust_info:
            info_dict = {}
            name = info.cust_name
            id = info.id
            info_dict['id'] = id
            info_dict['name'] = name
            info_lt.append(info_dict)
        user_info = UserInfo.objects.all()
        pur_orders = Purchase.objects.filter(is_finished=False).filter(is_delete=False).all()
        for usr in user_info:
            usr_lt.append(usr.user_name)
        data['cust_info'] = info_lt
        data['user_info'] = usr_lt
        data['pur_orders'] = pur_orders
        return render(request, 'create_purchase_order.html', data)
    # 输入地区并获取对应相应的客户名，ajax请求
    location = request.POST.get('location')
    if location:
        cust_info = CustomerInfo.objects.filter(cust_local__contains=location)
    else:
        cust_info = CustomerInfo.objects.all()
    for info in cust_info:
        info_dict = {}
        name = info.cust_name
        id = info.id
        info_dict['id'] = id
        info_dict['name'] = name
        info_lt.append(info_dict)
    data['cust_info'] = info_lt
    return JsonResponse(data)


def create_purchase_order(request):
    '''创建订单信息'''
    forms = PurchaseOrderFroms(request.POST)
    if forms.is_valid():
        forms.save()
    return redirect('/purchase/show_pur_order/')


def delete_purchase_order(request):
    id = request.POST.get('id').split('_')[-1]
    pur_info = Purchase.objects.filter(pk=id).first()
    pur_info.is_delete = True
    pur_info.save()
    data = {'code1': '888'}
    return JsonResponse(data)


def edit_purchase_order(request):
    count = 0
    price = 0
    ord_id = request.GET.get('ord_id')
    order_info = Purchase.objects.filter(pk=ord_id)
    pur_detail = PurchaseDetail.objects.filter(pur_id_id=ord_id)
    if order_info:
        order = order_info.first()
        order_detail = pur_detail.all().order_by('pur_pro_id')
        for i in order_detail:
            count += i.pur_pro_count
            price += i.pur_pro_price
        order.pur_price = price
        order.save()
        data = {
            'order': order,
            'order_detail': order_detail,
            'count': count,
            'price': price,
        }
        return render(request, 'edit_purchase_order.html', data)


def create_purchase_detail(request):
    ord_id = request.GET.get('ord_id')
    pro_id = request.POST.get('pro_id')
    pro_count = request.POST.get('pro_count')
    # 上传订单文件
    excel_file = request.FILES.get('file_in')
    if excel_file or (pro_id and pro_count):
        if excel_file:
            order_info = Purchase.objects.filter(pk=ord_id).first()
            cust_name = order_info.pur_cust_name
            # 调用订单写入函数，自动创建文件和文件名
            file_path = file_manage.output_purchase_file(cust_name, excel_file)
            # 订单写入函数
            pur_detail_lt = load_purchase_detail(file_path, 0)
            for i in pur_detail_lt:
                pro_id = i[0]
                pro_count = i[1]
                purchase_detail = purchase_detail_input(pro_id, int(ord_id), pro_count)
                purchase_detail.save()
            return redirect('/purchase/edit_pur_order/?ord_id=' + ord_id)
        purchase_detail = purchase_detail_input(pro_id, int(ord_id), pro_count)
        purchase_detail.save()
    return redirect('/purchase/edit_pur_order/?ord_id=' + ord_id)


def del_order_detail(request):
    ord_id = request.GET.get('ord_id')
    pur_pro_id = request.GET.get('pur_pro_id')
    print(pur_pro_id, pur_pro_id)
    pur_pro_info = PurchaseDetail.objects.filter(pur_pro_id=pur_pro_id).filter(pur_id_id=ord_id)
    if pur_pro_info:
        pur_pro_info.first().delete()
    return redirect('/purchase/edit_pur_order/?ord_id=' + ord_id)

