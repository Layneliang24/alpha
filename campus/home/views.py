from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import forms
from django.views.generic import UpdateView
from post import forms as post_forms
from login import models as login_models
from main import models
from main.views import CategoryView


def empty(request):
    return redirect('home:profile')


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class CenterView(CategoryView):
    # 模板位置
    template_name = 'home/center.html'
    model = models.Article

    def get_queryset(self):  # 默认是文章列表视图
        self.articles = self.model.objects.filter(author_id=self.request.user.id)
        page, paginator, page_range = self.get_page(self.articles, 10)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['item'] = 'Article'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class CenterFileView(CategoryView):
    # 模板位置
    template_name = 'home/center.html'

    def get_queryset(self):
        my_files = models.File.objects.filter(author_id=self.request.user.id)
        page, paginator, page_range = self.get_page(my_files, 10)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['item'] = 'File'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class CenterLinkView(CenterView):
    # 模板位置
    template_name = 'home/center.html'

    def get_queryset(self):
        my_links = models.Link.objects.filter(author_id=self.request.user.id)
        page, paginator, page_range = self.get_page(my_links, 10)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['item'] = 'Link'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class SearchArticleView(CenterView):
    template_name = 'home/center.html'

    def get_queryset(self):  # 默认是文章列表视图
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            self.articles = models.Article.objects.filter(title__icontains=keyword)
        page, paginator, page_range = self.get_page(self.articles, 10)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_queryset().get('keyword')
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class SearchFileView(CenterView):
    template_name = 'home/center.html'

    def get_queryset(self):  # 默认是文章列表视图
        my_files = models.File.objects.filter(author_id=self.request.user.id)
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            my_files = models.File.objects.filter(name__icontains=keyword)
        page, paginator, page_range = self.get_page(my_files, 10)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_queryset().get('keyword')
        context['item'] = 'File'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class SearchLinkView(CenterView):
    template_name = 'home/center.html'

    def get_queryset(self):  # 默认是文章列表视图
        my_links = models.Link.objects.filter(author_id=self.request.user.id)
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            my_links = models.Link.objects.filter(name__icontains=keyword)
        page, paginator, page_range = self.get_page(my_links, 10)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_queryset().get('keyword')
        context['item'] = 'Link'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class ProfileUpdateView(UpdateView):
    form_class = forms.ProfileForm
    model = login_models.Profile
    template_name = 'home/edit_profile.html'

    def get(self, request, **kwargs):
        self.object = login_models.Profile.objects.get(user_id=self.request.user.id)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('home:center')


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class ArticleUpdateView(UpdateView):
    form_class = post_forms.PostArticleForm
    model = models.Article
    template_name = 'home/edit_article.html'

    def get(self, request, **kwargs):
        self.object = super(ArticleUpdateView, self).get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('home:center')


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class LinkUpdateView(UpdateView):
    form_class = post_forms.PostLinkForm
    model = models.Link
    template_name = 'home/edit_link.html'

    def get(self, request, **kwargs):
        self.object = super(LinkUpdateView, self).get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('home:center')

