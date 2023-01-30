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

'''
Alen start
'''

class Goods(models.Model):       #商品主檔
    name = models.CharField(max_length=200)  #商品名
    price = models.IntegerField()            #價錢
    photo_url = models.CharField(max_length=255)  #照片連結
    create_date = models.DateField(auto_now_add=True)  #資料建議日
    
    class Meta:
        db_table = "goods"

class Member(models.Model):                          #會員帳號資料表
    accountname = models.CharField(max_length=50)    #帳號
    password = models.CharField(max_length=50)       #密碼
    username = models.CharField(max_length=50)       #會員姓名
    phonenumber = models.CharField(max_length=10)    #會員電話
    email = models.CharField(max_length=50)          #會員EMAIL
    address = models.CharField(max_length=255)       #會員地址

    class Meta:
        db_table = "member"

class OrdersModel(models.Model):
    subtotal = models.IntegerField(default=0)
    shipping = models.IntegerField(default=0)
    grandtotal = models.IntegerField(default=0)
    customname = models.CharField(max_length=100)
    customemail = models.CharField(max_length=100)
    customphone = models.CharField(max_length=50)
    paytype = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.customname

    class Meta:
        db_table = "ordersmodel"

class DetailModel(models.Model):
    dorder = models.ForeignKey('OrdersModel',on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    unitprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    dtotal = models.IntegerField(default=0)
    
    def __str__(self):
        return self.pname

    class Meta:
        db_table = "detailmodel"

class Orders(models.Model):
    dorder = models.ForeignKey('OrdersTotal',on_delete=models.CASCADE)    #訂單資料表 
    pname = models.CharField(max_length=100)                              #商品名稱
    unitprice = models.IntegerField(default=0)                            #單價
    quantity = models.IntegerField(default=0)                             #數量
    dtotal = models.IntegerField(default=0)                               #總價
    
    class Meta:
        db_table = "orders"

class OrdersTotal(models.Model):
	subtotal = models.IntegerField(default=0)
	shipping = models.IntegerField(default=0)
	grandtotal = models.IntegerField(default=0)
	custommail =  models.CharField(max_length=100)
	customphone =  models.CharField(max_length=50)
	paytype = models.CharField(max_length=20)
	create_date = models.DateTimeField(auto_now_add=True)
	ustomaddress = models.CharField(max_length=200)
	
	class Meta:
		db_table = "orderstotal"