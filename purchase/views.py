from django.shortcuts import render

# Create your views here.
from information.models import CustomerInfo, UserInfo
from purchase.models import Purchase


def purchase_manage(request):
    data = {}
    return render(request, 'purchase_manage.html', data)


def create_purchase_order(request):
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