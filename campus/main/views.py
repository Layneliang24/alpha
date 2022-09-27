from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout as sys_logout
from login.views import GetMethodMixin
from django.views import View
from django.views.generic import ListView
from . import models
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def empty(request):
    return redirect("main:index")


@login_required(login_url="login:login")
def logout(request):
    sys_logout(request)
    return redirect('login:login')


class NavView(View):
    def __init__(self):
        super().__init__()
        self.maincategory = models.MainCategory.objects.all()


@method_decorator(login_required(login_url="login:login"), name='dispatch')
# 将装饰器装饰到dispatch方法上，就相当于将装饰器装饰到该class的所有方法上
class IndexView(NavView):
    def get(self, request):
        maincategory = self.maincategory
        subcategory = models.SubCategory.objects.all()
        recommend = models.Article.objects.all().order_by('-views')[:8]
        link_list = models.Link.objects.all().order_by('-upload_time')[:13]
        file_list = models.File.objects.all().order_by('-upload_time')[:6]  # 获取最新的文件
        latest = models.Article.objects.all().order_by('-created')[:8]
        context = {
            'maincategory': maincategory,
            'subcategory': subcategory,
            'recommend' : recommend,
            'link_list': link_list,
            'file_list': file_list,
            'latest': latest,
        }
        return render(request, 'main/index.html', context)

    def post(self, request):
        keyword = request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            article_list = models.Article.objects.filter(title__icontains=keyword)
            page_num = request.GET.get('page')  # 使用request.GET.get()函数获取uri中的page参数的数值
            paginator = Paginator(articles, 6)  # 设置一页显示多少条数据（articles为要分页的数据）
            try:
                page = paginator.page(page_num)  # 获取当前的Page对象，该对象有页码、内容列表等属性
            except PageNotAnInteger:  # 如果用户输入的页码不是整数时,显示第1页的内容
                page = paginator.page(1)
            except (EmptyPage, InvalidPage):  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
                page = paginator.page(paginator.num_pages)
            return render(request, 'main/search.html', locals())


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
