from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def empty(request):
    return HttpResponse("跳转到profile")


def profile(request):
    return HttpResponse("访问profile")


def edit(request):
    return HttpResponse("编辑个人资料")


def articles(request):
    return HttpResponse("查看我的文章")


def files(request):
    return HttpResponse("查看我的文件")


def links(request):
    return HttpResponse("查看我的链接")


def reset(request):
    return HttpResponse("重置密码")
