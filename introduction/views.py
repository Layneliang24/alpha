from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def empty(request):
    return redirect('/introduction/index/')


def index(request):
    return HttpResponse("个人主页面")


def post(request):
    return HttpResponse("发布个人经历")


def edit(request):
    return HttpResponse("编辑个人经历")


def resume(request):
    return HttpResponse("个人简历")
