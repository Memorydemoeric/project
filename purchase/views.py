from copy import deepcopy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from common.DataProcess import file_manage
from common.DataProcess.database_input import purchase_detail_input
from common.DataProcess.excel_loads import load_purchase_detail
from common.DataProcess.translate import querydict_to_dict
from information.models import CustomerInfo, UserInfo
from purchase.forms import PurchaseOrderFroms
from purchase.helper import translate_order_detail, OrderDetail
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
        pur_orders = Purchase.objects.filter(is_finished=False).all()
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
    id = request.POST.get('cust_id')
    dic = querydict_to_dict(request.POST)
    dic['pur_location_name'] = CustomerInfo.objects.get(pk=id).cust_local
    forms = PurchaseOrderFroms(dic)
    if forms.is_valid():
        forms.save()
    return redirect('/purchase/show_pur_order/')


def edit_purchase_date(request):
    ord_id = request.POST.get('order_id')
    new_date = request.POST.get('new_date')
    purchase_info = Purchase.objects.get(pk=ord_id)
    purchase_info.pur_modify_date = new_date
    purchase_info.save()
    data = {
        'code1': '888',
    }
    return JsonResponse(data)


def delete_purchase_order(request):
    id = request.POST.get('id').split('_')[-1]
    pur_info = Purchase.objects.filter(pk=id).first()
    pur_info.delete()
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
        order_detail = pur_detail.all()
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
                purchase_detail_input(pro_id, int(ord_id), pro_count)
            return redirect('/purchase/edit_pur_order/?ord_id=' + ord_id)
        purchase_detail_input(pro_id, int(ord_id), pro_count)
    return redirect('/purchase/edit_pur_order/?ord_id=' + ord_id)


def del_order_detail(request):
    ord_id = request.GET.get('ord_id')
    pur_pro_id = request.GET.get('pur_pro_id')
    print(ord_id, pur_pro_id)
    pur_pro_info = PurchaseDetail.objects.filter(pur_pro_id_id=pur_pro_id).filter(pur_id_id=ord_id)
    if pur_pro_info:
        pur_pro_info.first().delete()
    return redirect('/purchase/edit_pur_order/?ord_id=' + ord_id)


def query_purchase(request):
    data = {}
    total_price = 0
    order_detail_lt = []
    if request.method == 'GET':
        order_infos = Purchase.objects.filter(is_finished=False).order_by('pur_modify_date')
        selected_order_detail = PurchaseDetail.objects.filter(pur_id__is_selected=1).filter(pur_id__is_finished=False).order_by('pur_pro_id')
        purchase_pro_lt = list(set(foo.pur_pro_id_id for foo in selected_order_detail))
        print(purchase_pro_lt)
        purchase_pro_dic = dict.fromkeys(purchase_pro_lt)
        for foo in selected_order_detail:
            if not purchase_pro_dic[foo.pur_pro_id_id]:
                purchase_pro_dic[foo.pur_pro_id_id] = [0, 0, 0, 0]
            purchase_pro_dic[foo.pur_pro_id_id][0] += foo.pur_pro_count
            purchase_pro_dic[foo.pur_pro_id_id][1] = foo.pur_pro_id.pro_count
            purchase_pro_dic[foo.pur_pro_id_id][2] = foo.pur_half_finished_id.half_count
        for foo in purchase_pro_dic:
            purchase_pro_dic[foo][3] = purchase_pro_dic[foo][1] + purchase_pro_dic[foo][2] - purchase_pro_dic[foo][0]
        for foo in order_infos:
            if foo.is_selected:
                total_price += foo.pur_price
        for index in sorted(purchase_pro_dic):
            purchase_pro = purchase_pro_dic[index]
            order_detail_lt.append(OrderDetail(index, purchase_pro[0], purchase_pro[1], purchase_pro[2], purchase_pro[3]))
        data['order_infos'] = order_infos
        data['total_price'] = total_price
        data['order_detail'] = order_detail_lt
        print(data)
        return render(request, 'query_purchase.html', data)


def select_purchase(request):
    data = {}
    all_select = request.POST.get('all_select')
    if all_select != None:
        Purchase.objects.all().update(is_selected=all_select)
        data['code'] = '888'
    else:
        id = request.POST.get('id')
        status = request.POST.get('status')
        Purchase.objects.filter(pk=id).update(is_selected=status)
        data['code'] = '888'
    return JsonResponse(data)
