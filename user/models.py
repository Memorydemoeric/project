from django.db import models

# Create your models here.


# 用户信息
class UserInfo(models.Model):
    user_name = models.CharField(max_length=32, unique=True, null=False)

    class Meta:
        db_table = 'syc_user_info'