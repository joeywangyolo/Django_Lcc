from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from Myapp.models import Acount
from django.contrib import auth
from django.contrib.auth import authenticate , login , logout
import datetime
 
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
        email = request.POST.get("email")
        # email = Acount.objects.get(email = email)
        try:
            acount = Acount.objects.get(name = username)
        except :
                return render(request,'login.html', {'msg':'帳號或密碼錯誤！'})                  
        if acount is not None :
                if acount.user == username :    
                    if acount.password == password:    
                        return render(request,'home.html',{'name':username,'email':acount.email,'today':today})
                else:
                    return render(request,'login.html', {'msg':'帳號或密碼錯誤！'}) 
                
    return render(request,'login.html', {'msg':'請輸入帳號及密碼'}) 
        
def register(request):
    return render(request, 'reg123.html')

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
   
    return render(request, 'home.html',{'email':email,'name':name})


def viewArticle(request, articleId):
    text = 'Display article Number : {}'.format(articleId)
    return HttpResponse(text)

