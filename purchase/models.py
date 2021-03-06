import datetime

from django.db import models

from information.models import CustomerInfo

# Create your models here.



# 订单
from storage.models import StorageProduct, StorageHalfFinished


class Purchase(models.Model):
    pur_location_name = models.CharField(max_length=64)
    pur_cust_name = models.CharField(max_length=64)
    pur_price = models.FloatField(default=0.00)
    pur_create_date = models.DateTimeField(auto_now_add=True)
    pur_modify_date = models.DateField(default= datetime.datetime.now().strftime('%Y-%m-%d'))
    pur_finished_date = models.DateField(auto_now=True)
    pur_handle = models.CharField(max_length=256)
    cust_id = models.ForeignKey(CustomerInfo, on_delete=models.PROTECT)
    is_selected = models.BooleanField(default=0)
    is_finished = models.BooleanField(default=0)

    class Meta:
        db_table = 'syc_purchase'


# 订单详情
class PurchaseDetail(models.Model):
    pur_pro_id = models.ForeignKey(StorageProduct, to_field='pro_id')
    pur_half_finished_id = models.ForeignKey(StorageHalfFinished, to_field='half_id')
    pur_pro_type = models.CharField(max_length=256, null=False)
    pur_pro_count = models.IntegerField(default=0)
    pur_finished_pro_count = models.IntegerField(default=0)
    pur_pro_unit_price = models.FloatField(default=0.00)
    pur_pro_price = models.FloatField(default=0.00)
    pur_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    class Meta:
        db_table = 'syc_pur_detail'