"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:`
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myapp import views
from django.urls import re_path as url

urlpatterns = [
        url(r'^about/', views.about, name='about'),     #關於我們
        url(r'^collections/', views.collections, name='collections'),    #服裝
        url(r'^cart/', views.cart, name='cart'),           #購物車
        url(r'^addtocartadd/(\d+)/',views.addtocartAdd, name='addtocartadd'), #加入購物車
        url(r'^addtocartupdate/',views.addtocartUpdate, name='addtocartupdate'), #更新購物車
        url(r'^addtocartempty/',views.addtocartEmpty, name='addtocartempty'), #清空購物車
        url(r'^addtocartremove/(\d+)/',views.addtocartRemove, name='addtocartremove'), #刪除單項商品
        url(r'^cartorder/',views.cartorder,name='cartorder'),
        url(r'^cartok/',views.cartok,name='cartok'),
        url(r'^cartordercheck/',views.cartordercheck,name = 'cartordercheck'),
        url(r'^hello/', views.hello, name='hello'),
        url(r'^article/(\d+)/', views.viewArticle, name='article'),
        url(r'^loginPage/',views.loginPage, name='login'),
        url(r'^reg/',views.reg, name='reg'),
        url(r'^regProcess/',views.regProcess, name='regProcess'),
        url(r'^forgotPassword/',views.forgotPassword, name='forgotPassword'),
        url(r'^logout/', views.logout, name='logout'),
        url(r'^getdata/', views.getdata, name='getdata'),
        url(r'', views.index, name='index'),           #首頁
]
