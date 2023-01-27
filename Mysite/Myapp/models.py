from django.db import models
# Create your models here.
class Dreamreal(models.Model):

    userName = models.CharField(max_length=10,null=False) #類別關聯
    password = models.CharField(max_length=20,null=False) #暱稱
    name = models.CharField(max_length=50,null=False) #信箱
    email = models.IntegerField(null=False) #手機號
    class Meta:
        db_table = 'dreamreal'

class Acount(models.Model):
    user = models.CharField(max_length=30,null=False)
    password = models.CharField(max_length=30,null=False)
    name = models.CharField(max_length=30,null=False)
    email = models.CharField(max_length=50,null=False)
    class Meta:
        db_table = 'Acount'

