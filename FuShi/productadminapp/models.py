from django.db import models

import userapp

# Create your models here.

class ProductAdmin(models.Model):
    '''
    产品管理模块
    '''
    id = models.AutoField(primary_key=True)
    # 产品名称
    pro_name = models.CharField(max_length=50)
    # 产品代码
    pro_code = models.IntegerField()
    # 产品类别
    pro_type = models.CharField(max_length=100)
    # 单价
    pro_price = models.FloatField(verbose_name='商品价格')
    # 库位
    pro_kuwei = models.IntegerField()
    # 备注
    pro_intro = models.TextField(verbose_name='产品备注')
    # 所属用户
    usertable = models.ForeignKey(userapp.models.UserTable, on_delete=models.CASCADE)

