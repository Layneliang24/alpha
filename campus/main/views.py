from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout as sys_logout
from django.views.generic import ListView
from . import models


def empty(request):
    return redirect("main:index")


@login_required(login_url="login:login")
def logout(request):
    sys_logout(request)
    return redirect('login:login')


@method_decorator(login_required(login_url="login:login"), name='dispatch')
# 将装饰器装饰到dispatch方法上，就相当于将装饰器装饰到该class的所有方法上
class IndexView(ListView):
    template_name = "main/index.html"
    subcategory = models.SubCategory.objects.all()
    context_object_name = ("maincategory")
    model = models.MainCategory


def categories(request):
    return HttpResponse("查看分类详情")


def articles(request):
    return HttpResponse("查看文章详情")


def files(request):
    return HttpResponse("查看文件列表")


def links(request):
    return HttpResponse("查看链接列表")


def search(request):
    return HttpResponse("搜索文章/文件/链接")
