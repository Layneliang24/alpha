from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def empty(request):
    return HttpResponse("访问登录页面，要避免重定向过多问题")  # 输入空字符串就会跳转到login页面


def login(request):
    return HttpResponse("访问登录页面")


def register(request):
    return HttpResponse("访问注册页面")


def logout(request):
    return redirect('/login/')


def confirm(request):
    return HttpResponse("用户确认页面")
