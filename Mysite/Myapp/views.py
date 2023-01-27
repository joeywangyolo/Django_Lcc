from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from Myapp.models import Acount
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
            acount = Acount.objects.get(name = username)
        except :
                return render(request,'login.html', {'msg':'帳號或密碼錯誤！'})                  
        if acount is not None :
                if acount.user == username :    
                    if acount.password == password: 
                        # request.session['username'] = username
                        return render(request,'home.html',{'name':username,'email':acount.email,'today':today})
                else:
                    return render(request,'login.html', {'msg':'帳號或密碼錯誤！'}) 
                
    return render(request,'login.html', {'msg':'請輸入帳號及密碼'}) 

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "home.html")      

def register(request):
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


    
