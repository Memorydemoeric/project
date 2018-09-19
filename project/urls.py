"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from information import views as information_views
from purchase import views as purchase_views
from report import views as report_views
from sales import views as sales_viwes
from storage import views as storage_views
from system import views as system_views

urlpatterns = [
    url(r'^purchase/$', purchase_views.purchase_manage),
    url(r'^sales/', sales_viwes.sales_manage),
    url(r'^storage/', storage_views.storage_manage),
    url(r'^report/', report_views.report_manage),
    url(r'^info/', information_views.info_manage),
    url(r'^system/', system_views.system_manage),
    url(r'^purchase/create_pur_order/', purchase_views.create_purchase_order),
    url(r'^purchase/show_pur_order/', purchase_views.show_purchase_order),
    url(r'^purchase/edit_pur_order/', purchase_views.edit_purchase_order),
    url(r'^purchase/edit_pur_date/', purchase_views.edit_purchase_date),
    url(r'^purchase/delete_pur_order/', purchase_views.delete_purchase_order),
    url(r'^purchase/create_pur_detail/', purchase_views.create_purchase_detail),
    url(r'^purchase/del_order_detail/', purchase_views.del_order_detail),
    url(r'^purchase/query_purchase/', purchase_views.query_purchase),
    url(r'^purchase/select_purchase/', purchase_views.select_purchase),





    url(r'^input_cust_info/', information_views.input_cust_info),
    url(r'^input_pro_info/', storage_views.input_pro_info),
    url(r'^input_half_pro_info/', storage_views.input_half_pro_info),
]





