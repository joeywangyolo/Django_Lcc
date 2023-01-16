from django.db import models
# Create your models here.
class Dreamreal(models.Model):

    website = models.CharField(max_length=10,null=False) #類別關聯
    nickname = models.CharField(max_length=20,null=False) #暱稱
    mail = models.CharField(max_length=50,null=False) #信箱
    phonenumber = models.IntegerField(null=False) #手機號
    class Meta:
        db_table = 'dreamreal'

class Acount(models.Model):
    user = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = 'Acount'

