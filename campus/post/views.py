from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def empty(request):
    return redirect('/post/article/')


def post(request):
    pass


def article(request):
    return HttpResponse("发布文章")


def file(request):
    return HttpResponse("发布文件")


def link(request):
    return HttpResponse("发布链接")

