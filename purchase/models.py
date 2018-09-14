import datetime

from django.db import models

# Create your models here.

# 订单
from customer.models import CustomerInfo


class Purchase(models.Model):
    pur_location_name = models.CharField(max_length=64)
    pur_cust_name = models.CharField(max_length=64)
    pur_price = models.FloatField(default=0.00)
    pur_create_date = models.DateTimeField(auto_now_add=True)
    pur_modify_date = models.DateField(default= datetime.datetime.now().strftime('%Y-%m-%d'))
    pur_finished_date = models.DateField(auto_now=True)
    pur_handle = models.CharField(max_length=256)
    cust_id = models.ForeignKey(CustomerInfo, on_delete=models.PROTECT)
    is_finished = models.BooleanField(default=0)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'syc_purchase'


# 订单详情
class PurchaseDetail(models.Model):
    pur_pro_id = models.CharField(max_length=64, null=False)
    pur_pro_type = models.CharField(max_length=256, null=False)
    pur_pro_count = models.IntegerField(default=0)
    pur_finished_pro_count = models.IntegerField(default=0)
    pur_pro_unit_price = models.FloatField(default=0.00)
    pur_pro_price = models.FloatField(default=0.00)
    pur_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'syc_pur_detail'