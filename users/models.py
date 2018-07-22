# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    name = models.CharField("姓名", max_length=10,default="")
    password = models.CharField("密码", max_length=50, default="")
    student_id = models.IntegerField("学号",default=0)
    grade = models.IntegerField("年级",default=0)
    major = models.CharField("专业", max_length=50,default="")
    email = models.CharField("邮箱", max_length=50,default="")

    class Meta:
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.name





