from django.db import models

# Create your models here.


# 成品库存
class StorageProduct(models.Model):
    pro_id = models.CharField(max_length=64, unique=True, null=False)
    pro_type = models.CharField(max_length=256, null=False)
    pro_count = models.IntegerField(default=0)
    pro_cost_unit_price = models.FloatField(default=0)
    pro_sell_unit_price = models.FloatField(default=0)
    pro_sell_price = models.FloatField(default=0.00)
    pro_heading_code = models.CharField(max_length=64, default='-')
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'syc_stor_product'


# 半成品库存
class StorageHalfFinished(models.Model):
    half_id = models.CharField(max_length=64, unique=True, null=False)
    half_type = models.CharField(max_length=256, null=False)
    half_count = models.IntegerField(default=0)
    half_cost_unit_price = models.FloatField(default=0.00)
    half_sell_unit_price = models.FloatField(default=0.00)
    half_sell_price = models.FloatField(default=0.00)
    half_heading_code = models.CharField(max_length=64, default='-')
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'syc_stor_half_finished'