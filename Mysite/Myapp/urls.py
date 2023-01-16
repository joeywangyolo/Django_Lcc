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
        url(r'^hello/', views.hello, name='hello'),
        url(r'^article/(\d+)/', views.viewArticle, name='article'),
        url(r'^loginPage/',views.loginPage, name='login'),
        url(r'^reg/',views.register, name='register'),
        url(r'^regProcess/',views.regProcess, name='regProcess'),
        # url(r'^sendHttpEmail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', views.sendHttpEmail,
        # name='sendHttpEmail'),
]
