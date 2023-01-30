from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from Myapp.models import Acount, models, Goods, OrdersModel, DetailModel
from django.contrib import auth
import datetime
from django.core.mail import send_mail

def hello(request):
    today = datetime.datetime.now().date()
    name = request.POST.get("name")
    return render(request, 'home.html',{'today':today,'name':name})

def loginPage(request):
    state = 'not logged in'
    today = datetime.datetime.now().date()
    if request.method == "POST":
        username = request.POST.get("user",None)
        password = request.POST.get("password",None)
        # email = Acount.objects.get(email = email)
        try:
            acount = Acount.objects.get(user = username)
        except :
            return render(request,'login.html', {'msg':'帳號或密碼錯誤！'})                  
        if acount is not None :
                if acount.user == username :    
                    if acount.password == password: 
                        request.session['username'] = username
                        #return render(request,'home.html',{'name':username,'email':acount.email,'today':today})
                        return render(request,'index.html')
                else:
                    return render(request,'login.html', {'msg':'帳號或密碼錯誤！'}) 
                
    return render(request,'login.html', {'msg':'請輸入帳號及密碼'}) 

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "index.html")      

def reg(request):
    return render(request, 'signup1.html',{'msg':'請輸入您的註冊資訊'})

def regProcess(request):
    user = request.POST.get("user")
    password = request.POST.get("password")
    name = request.POST.get("name")
    email = request.POST.get("email")
    
    newAcount = Acount(
        user=user,
        password=password,
        name=name,
        email=email
        )
    newAcount.save()
    # send_mail(
    #     "Hello {} 帳號已註冊".format(name), 
    #     "感謝您註冊本系統，若有任何疑問請聯繫客服人員！", 
    #     'joeywang45@gmail.com',
    #     [email],
    #     html_message = '<p>This is an <strong>important</strong> message.</p>')
    return render(request, 'home.html',{'email':email,'name':name})
    # return render(request, 'index.html')
    # return HttpResponse(user+password+name+email)


def viewArticle(request, articleId):
    text = 'Display article Number : {}'.format(articleId)
    return HttpResponse(text)

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get("email",None)
        # Acount = Acount.objects.get(email = email)
        try:
            acount = Acount.objects.get(email = email)
        except :
                return render(request,'forgotPassword.html', {'msg':'查無此帳號312！'})
        if email is not None :
                if acount.email == email :        
                        return render(request,'forgotPassword.html',{'msg':'你的密碼是 -->{}'.format(acount.password)})
                else:
                    return render(request,'forgotPassword.html', {'msg':'查無此帳號！'})

    return render(request,'forgotPassword.html', {'msg':'請輸入你的 email !'})

'''
Alen start
'''

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

'''
Alen get data test
'''

from bs4 import BeautifulSoup
import requests

def getdata(request):
    g_today = datetime.date.today()
    url = requests.get('https://www.hitobp.com.tw/product_category?store_type_sn=64&category_sn=1892')

    if url.status_code == 200:
        soup = BeautifulSoup(url.text,'html.parser')
        titles = soup.select('div.product_name.ds_product_caption_color.ds_product_caption_size.has_cta h2')
        priecs = soup.select('span.activity_price.ds_product_price_activity_size.ds_product_price_activity_color')
        image = soup.select('a.pd_item_pic.ds_product_pic_H img.pic_img.lazy')
    
    num = 0
    for title,price,img in zip(titles,priecs,image):
        name = title.text
        price = int(price.text.replace('$',''))
        photo_url = img.get('src')
        num += 1

        newData = Goods(
        id = num,
        user=name,
        price=price,
        photo_url=photo_url,
        create_date=g_today
        )
        newData.save()

    return HttpResponse('123')


def collections(request):
    allGoods = Goods.objects.all().order_by('id')
    # allGoods = {'name':'55688','price':'147','photo_url':'https://photo.hitobp.com.tw/photo/K3060008-E.jpg'}
    return render(request,'product.html',locals())


cartlist = list() # 購物車的內容
customname = "" #客戶姓名
customphone = "" #客戶電話
customaddress = "" #客戶地址
customemail = "" # 客戶email

orderTotal = 0 # 消費總額
goodsTitle = list() # 存放放入購物車的商品名稱

# 這個是加入到購物車中，並未將商品資訊寫入至資料庫中
def addtocartAdd(request,productid=None,ctype='add'):
    global cartlist
    
    if ctype=="add":  # 將商品加入至購物車中
        product = Goods.objects.get(id=productid)  
        flag = True  # 預設購物車中沒有相同的商品，表示購物車內這個商品不存在
        
        #檢查購物車中的商品是否有重覆
        for unit in cartlist:
            if product.name == unit[0]:  # 表示有這個商品
                unit[2] = str(int(unit[2]) + 1) #數量再加1
                unit[3] = str(int(unit[3]) + product.price) # 累計金額
                flag = False # 表示商品之前已經加入至購物車中
                break

        if flag:  # 在購物車中沒有此商品
            templist = list()
            templist.append(product.name)
            templist.append(str(product.price))
            templist.append('1')             #需考慮數量變動(第一次加入購物車的數量)
            templist.append(str(product.price))
            cartlist.append(templist)
        
        request.session['cartlist'] = cartlist 
        return redirect('cart')

#更新購物車
def addtocartUpdate(request,ctype='update'):
    global cartlist
    if ctype == "update":  #修改購物車數量
        n = 0
        for unit in cartlist:  #先將購物車內容抓出並修改數量總價
            amount = request.POST.get('qty'+str(n),'1')
            if len(amount) == 0:
                amount = '1'
            if int(amount) <= 0:
                amount = '1'

            unit[2] = amount   #抓取qty0以此類推，預設數量為1
            unit[3] = str(int(unit[1]) * int(unit[2]))
            n += 1

        request.session['cartlist'] = cartlist
        return redirect('cart')

#清空購物車
def addtocartEmpty(request,ctype='empty'):
    global cartlist
    if ctype == "empty":
        cartlist = list()
        request.session['cartlist'] = cartlist
        return redirect('cart')

#刪除商品
def addtocartRemove(request,productid=None,ctype='remove'):
    if ctype == 'remove':
        del cartlist[int(productid)]   #將對應商品id刪除
        request.session['cartlist'] = cartlist
        return redirect('cart')

# 顯示購物車內容
def cart(request):  
    global cartlist
    allcart = cartlist
    total = 0
    for unit in cartlist:
        total += int(unit[3])
    grandtotal = total + 100  # 預設運費為100元
    return render(request,'cart.html',locals())



def cartorder(request):   #結帳
    #當要結帳時。要先登入才可結帳
    global cartlist,customname,customphone,customaddress,customemail
    total = 0
    allcart = cartlist
    for unit in cartlist:
        total += int(unit[3])
    grandtotal = total + 100  #運費

    name = customname
    phone = customphone
    address = customaddress
    email = customemail

    return render(request,'cartorder.html', locals()) 

#已確認資料並送。所以會將訂單寫入資料庫
def cartok(request):     
    global cartlist,customname,customphone,customaddress,customemail
    global orderTotal,goodsTitle

    total = 0
    for unit in cartlist:
        total += int(unit[3])

    grandtotal = total + 100  #運費

    orderTotal = grandtotal
    customname = request.POST.get('cuName','')
    customemail = request.POST.get('cuEmail','')
    customphone = request.POST.get('cuPhone','')
    customaddress = request.POST.get('cuAdder','')
    payType = request.POST.get('payType','')

    unitorder = OrdersModel.objects.create(subtotal=total,shipping=100,grandtotal=grandtotal,customname=customname,customemail=customemail,customphone=customphone,paytype=payType)

        #要將各個的商品新增到 明細表
    for unit in cartlist:
        goodsTitle.append(unit[0]) # 將要買的商品名稱新增至goodsTitle中
        total = int(unit[1]) * int(unit[2])
        unitdetail = DetailModel.objects.create(dorder=unitorder,pname=unit[0],unitprice=unit[1],quantity=unit[2],dtotal=total)
        
    orderid = unitorder.id   # 取得訂單編號
    name = unitorder.customname
    email = unitorder.customemail
    cartlist = list()
    request.session['cartlist'] = cartlist

    return render(request,'cartok.html',locals())  

#已完成訂單，做訂單查詢。
def cartordercheck(request):    
    orderid = request.GET.get('orderid','')
    customemail = request.GET.get('customemail','')
    
    if orderid == '' and customemail == '':
    #if orderid == '':
        nosearch = 1
    else:
        order = OrdersModel.objects.filter(id=orderid).first() # 抓第一筆資料
        if order == None:
            notfound = 1
        else:
            details = DetailModel.objects.filter(dorder=order)
    return render(request,"cartordercheck.html",locals())
