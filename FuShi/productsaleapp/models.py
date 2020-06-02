from django.db import models

import productadminapp
# Create your models here.


class ProductSale(models.Model):
    '''
    产品销售
    '''
    id = models.AutoField(primary_key=True)
    # 客户姓名
    name = models.CharField(max_length=50,verbose_name='客户姓名')
    # 客户手机
    phone_number = models.CharField(max_length=12)
    # 销售单价
    sale_price = models.FloatField(verbose_name='销售单价')
    # 销售数量
    sale_number =  models.IntegerField()
    # 合计金额
    total_money = models.FloatField(verbose_name='合计金额')
    # 备注
    pro_info = models.TextField(verbose_name='备注')
    # 和产品管理模块关联
    product = models.ForeignKey(productadminapp.models.ProductAdmin, on_delete=models.CASCADE)