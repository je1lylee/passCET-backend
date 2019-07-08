from django.db import models

# Create your models here.
# 用户表
class passcet_user(models.Model):
    name = models.CharField(max_length=30) #昵称
    email = models.CharField(max_length=40, null=True) #email 电话和邮件有一个即可
    phone = models.IntegerField(null=True) #电话号码
    leavel = models.IntegerField(null=False,default=0) #学习等级 0为未设置 4是band4 6是band6

#邮箱验证码
class passcet_emailcode(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    time = models.FloatField(default=0)