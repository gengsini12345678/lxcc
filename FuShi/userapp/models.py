from datetime import datetime

from django.db import models

from  django.contrib.auth.models import User

# Create your models here.


class UserTable(models.Model):
    '''
    用户数据模型
    '''
    id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=50)
    # userpass = models.CharField(max_length=100)
    realname = models.CharField(max_length=50, default='请完善')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
