from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class UserProfile(AbstractUser):
    name = models.CharField("姓名",max_length=30, null=True, blank=True)
    mobile = models.CharField("电话",max_length=11,null=True,blank=True)
    email = models.EmailField("邮箱",max_length=100, null=True, blank=True)
    is_org = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    code = models.CharField("验证码",max_length=10)
    mobile = models.CharField("电话",max_length=11)
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
    

class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码')
    )
    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name