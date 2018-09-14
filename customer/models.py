from django.db import models

# Create your models here.


# 客户信息
class CustomerInfo(models.Model):
    cust_name = models.CharField(max_length=64, null=False)
    cust_local = models.CharField(max_length=256, null=False)
    cust_mobile_phone = models.CharField(max_length=32, default='-')
    cust_phone_number = models.CharField(max_length=32, default='-')
    cust_rebate = models.FloatField(default=100.00)
    cust_address = models.CharField(max_length=1024)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'syc_cust_info'