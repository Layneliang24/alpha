from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def empty(request):
    return redirect("/main/index/")


def index(request):
    return HttpResponse("访问index")


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


