from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from login import models as login_models
from main import models
from main.views import IndexView
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


# Create your views here.
def empty(request):
    return redirect('home:profile')


class CenterView(IndexView):
    # 模板位置
    template_name = 'home/center.html'

    def get_queryset(self):     # 默认是文章列表视图
        my_profile = login_models.Profile.objects.get(user_id=self.request.user.id)
        self.articles = models.Article.objects.filter(author_id=self.request.user.id)
        user_article_count = models.Article.objects.filter(author_id=self.request.user.id).count()
        user_file_count = models.File.objects.filter(author_id=self.request.user.id).count()
        user_link_count = models.Link.objects.filter(author_id=self.request.user.id).count()
        page_num = self.request.GET.get('page', 1)  # 使用request.GET.get()函数获取uri中的page参数的数值
        paginator = Paginator(self.articles, 10)  # 设置一页显示多少条数据（articles为要分页的数据）
        page_range = list(range(max(int(page_num) - 2, 1), int(page_num))) + list(
            range(int(page_num), min(int(page_num) + 2, paginator.num_pages) + 1))
        # 加上省略页码标记
        if page_range[0] - 1 >= 2:
            page_range.insert(0, '...')
        if paginator.num_pages - page_range[-1] >= 2:
            page_range.append('...')
        # 加上首页和尾页
        if page_range[0] != 1:
            page_range.insert(0, 1)
        if page_range[-1] != paginator.num_pages:
            page_range.append(paginator.num_pages)
        try:
            page = paginator.page(page_num)  # 获取当前页码的记录
        except PageNotAnInteger:  # 如果用户输入的页码不是整数时,显示第1页的内容
            page = paginator.page(1)
        except (EmptyPage, InvalidPage):  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
            page = paginator.page(paginator.num_pages)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_queryset().get('my_profile')
        context['page'] = self.get_queryset().get('page')
        context['page_range'] = self.get_queryset().get('page_range')
        context['paginator'] = self.get_queryset().get('paginator')
        context['user_article_count'] = self.get_queryset().get('user_article_count', 0)
        context['user_file_count'] = self.get_queryset().get('user_file_count', 0)
        context['user_link_count'] = self.get_queryset().get('user_link_count', 0)
        return context


class CenterFileView(IndexView):
    # 模板位置
    template_name = 'home/center-file.html'

    def get_queryset(self):
        my_profile = login_models.Profile.objects.get(user_id=self.request.user.id)
        self.files = models.File.objects.filter(author_id=self.request.user.id)
        user_article_count = models.Article.objects.filter(author_id=self.request.user.id).count()
        user_file_count = models.File.objects.filter(author_id=self.request.user.id).count()
        user_link_count = models.Link.objects.filter(author_id=self.request.user.id).count()
        page_num = self.request.GET.get('page', 8)  # 使用request.GET.get()函数获取uri中的page参数的数值
        paginator = Paginator(self.files, 1)  # 设置一页显示多少条数据（articles为要分页的数据）
        page_range = list(range(max(int(page_num) - 2, 1), int(page_num))) + list(
            range(int(page_num), min(int(page_num) + 2, paginator.num_pages) + 1))
        # 加上省略页码标记
        if page_range[0] - 1 >= 2:
            page_range.insert(0, '...')
        if paginator.num_pages - page_range[-1] >= 2:
            page_range.append('...')
        # 加上首页和尾页
        if page_range[0] != 1:
            page_range.insert(0, 1)
        if page_range[-1] != paginator.num_pages:
            page_range.append(paginator.num_pages)
        try:
            page = paginator.page(page_num)  # 获取当前页码的记录
        except PageNotAnInteger:  # 如果用户输入的页码不是整数时,显示第1页的内容
            page = paginator.page(1)
        except (EmptyPage, InvalidPage):  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
            page = paginator.page(paginator.num_pages)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_queryset().get('my_profile')
        context['page'] = self.get_queryset().get('page')
        context['page_range'] = self.get_queryset().get('page_range')
        context['paginator'] = self.get_queryset().get('paginator')
        context['user_article_count'] = self.get_queryset().get('user_article_count', 0)
        context['user_file_count'] = self.get_queryset().get('user_file_count', 0)
        context['user_link_count'] = self.get_queryset().get('user_link_count', 0)
        return context


class CenterLinkView(CenterView):
    # 模板位置
    template_name = 'home/center-link.html'


@login_required(login_url="login:login")
def profile(request):
    my_profile = login_models.Profile.objects.get(user_id=request.user.id)
    if request.method == "POST":
        # 文章表中有数据和文件，文件需要用request.FILES获取
        profile_form = forms.ProfileForm(request.POST, request.FILES)
        bad_message = 'Oops, something wrong, please check and fill in the blank(s)!'
        if profile_form.is_valid():  # 确保所有的内容都不为空
            gender = profile_form.cleaned_data['gender']
            nickname = profile_form.cleaned_data['nickname']
            resume = profile_form.cleaned_data['resume']
            phone = profile_form.cleaned_data['phone']
            my_profile.gender = gender
            my_profile.nickname = nickname
            my_profile.resume = resume
            my_profile.phone = phone
            if 'portrait' in request.FILES:  # 如果用户更改了头像的话，才覆盖，因为更改头像不是必须的，用户可能没上传头像，那么会导致头像是空白的
                my_profile.portrait = profile_form.cleaned_data['portrait']
            my_profile.save()
            good_message = 'Save change success!'
            context = {'profile': my_profile, 'form': profile_form, 'good_message': good_message}
            return render(request, 'home/profile.html', context)
        else:
            context = {'profile': my_profile, 'form': profile_form, 'bad_message': bad_message}
            return render(request, 'home/profile.html', context)
    profile_form = forms.ProfileForm  # 干啥用?对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据
    context = {'profile': my_profile, 'form': profile_form}
    return render(request, 'home/profile.html', context)


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
