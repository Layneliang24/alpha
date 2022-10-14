from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout as sys_logout
from django.views import View
from django.views.generic import ListView, DetailView
from . import models
from login import models as login_models
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import markdown
from django.contrib.auth.models import User


def empty(request):
    return redirect("main:indexview")


@login_required(login_url="login:login")
def logout(request):
    sys_logout(request)
    return redirect('login:login')


class NavView(View):
    def __init__(self):
        super().__init__()
        self.maincategory = models.MainCategory.objects.all()
        self.subcategory = models.SubCategory.objects.all()
        self.articles = models.Article.objects.all()

    def get_login_profile(self):
        profile = login_models.Profile.objects.get(user_id=self.request.user.id)
        return profile

    def get_user_data(self):
        user_article_count = models.Article.objects.filter(author_id=self.request.user.id).count()
        user_file_count = models.File.objects.filter(author_id=self.request.user.id).count()
        user_link_count = models.Link.objects.filter(author_id=self.request.user.id).count()
        return user_article_count, user_file_count, user_link_count

    def get_page(self, items, set_num):
        page_num = self.request.GET.get('page', 1)  # 使用request.GET.get()函数获取uri中的page参数的数值
        paginator = Paginator(items, set_num)  # 设置一页显示多少条数据（articles为要分页的数据）
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
        return page, paginator, page_range


@method_decorator(login_required(login_url="login:login"), name='dispatch')
# 将装饰器装饰到dispatch方法上，就相当于将装饰器装饰到该class的所有方法上
class IndexView(NavView, ListView):
    # 模板位置
    template_name = 'main/index.html'

    # 加上这一行，告知允许哪种请求方式
    # http_method_names = ['GET', 'POST']

    def get_queryset(self):  # 重写get_queryset方法
        recommend = models.Article.objects.all().order_by('-views')[:8]
        link_list = models.Link.objects.all().order_by('-upload_time')[:12]
        file_list = models.File.objects.all().order_by('-upload_time')[:7]  # 获取最新的文件
        latest = models.Article.objects.all().order_by('-created')[:8]
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        # 很关键，必须把原方法的结果拿到
        context = super().get_context_data(**kwargs)
        context['maincategory'] = self.maincategory
        context['subcategory'] = self.subcategory
        context['profile'] = self.get_login_profile()
        context['recommend'] = self.get_queryset().get('recommend')
        context['link_list'] = self.get_queryset().get('link_list')
        context['file_list'] = self.get_queryset().get('file_list')  # 获取最新的文件
        context['latest'] = self.get_queryset().get('latest')
        context['user_article_count'] = self.get_user_data()[0]
        context['user_file_count'] = self.get_user_data()[1]
        context['user_link_count'] = self.get_user_data()[2]
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class CategoryView(IndexView):
    # 模板位置
    template_name = 'main/category.html'
    pk_url_kwarg = 'category_id'
    model = models.Article

    def get_queryset(self):  # 重写get_queryset方法
        self.articles = self.model.objects.filter(category=self.request.GET.get('category', 7))
        cat_id = self.request.GET.get('category', 1)
        page, paginator, page_range = self.get_page(self.articles, 10)
        return locals()

    # 重写get_context_data方法
    def get_context_data(self, **kwargs):
        # 很关键，必须把原方法的上下文结果拿到
        context = super().get_context_data(**kwargs)
        context['cat_id'] = self.get_queryset().get('cat_id')
        context['page'] = self.get_queryset().get('page')
        context['paginator'] = self.get_queryset().get('paginator')
        context['page_range'] = self.get_queryset().get('page_range')
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class ArticleView(NavView, DetailView):
    # 模板位置
    model = models.Article
    template_name = "main/article.html"
    context_object_name = "article"
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        """
        获取需要展示的对象
        """
        # 首先调用父类的方法
        article = super(ArticleView, self).get_object()
        md = markdown.Markdown(
            extensions=[
                # 包含 缩写、表格等常用扩展
                'markdown.extensions.extra',
                # 语法高亮扩展
                'markdown.extensions.codehilite',
                # 目录扩展
                'markdown.extensions.toc',
                'markdown.extensions.tables',
            ]
        )
        article.body = md.convert(article.body)
        # 浏览量 +1
        article.views = article.views + 1
        article.save(update_fields=['views'])
        return article

    # 重写get_context_data方法
    def get_context_data(self, **kwargs):
        # 很关键，必须把原方法的结果拿到
        context = super().get_context_data(**kwargs)
        context['maincategory'] = self.maincategory
        context['subcategory'] = self.subcategory
        context['profile'] = self.get_login_profile()
        context['files'] = models.File.objects.filter(article_id=self.get_object().id)
        # 获取当前文章的上一篇和下一篇
        context['previous_article'] = models.Article.objects.filter(id__gt=self.get_object().id,
                                                                    category=self.get_object().category.id).last()
        context['next_article'] = models.Article.objects.filter(id__lt=self.get_object().id,
                                                                category=self.get_object().category.id).first()
        context['user_article_count'] = self.get_user_data()[0]
        context['user_file_count'] = self.get_user_data()[1]
        context['user_link_count'] = self.get_user_data()[2]
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class VisitArticleView(NavView, DetailView):
    # 模板位置
    model = User
    template_name = "home/center_for_visitor.html"
    context_object_name = "profile_for_visitor"
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        """
        获取需要展示的对象
        """
        # 首先调用父类的方法
        user = super(VisitArticleView, self).get_object()
        return user

    def get_host_data(self):  # 获取主人的资料
        articles = models.Article.objects.filter(author_id=self.get_object().id)
        page, paginator, page_range = self.get_page(articles, 10)
        return locals()

    # 重写get_context_data方法
    def get_context_data(self, **kwargs):
        # 很关键，必须把原方法的结果拿到
        context = super().get_context_data(**kwargs)
        context['maincategory'] = models.MainCategory.objects.all()
        context['subcategory'] = models.SubCategory.objects.all()
        context['profile'] = self.get_login_profile()
        context['profile_for_visitor'] = login_models.Profile.objects.get(user_id=self.get_object().id)
        context['user_article_count'] = self.get_user_data()[0]
        context['user_file_count'] = self.get_user_data()[1]
        context['user_link_count'] = self.get_user_data()[2]
        context['page'] = self.get_host_data().get('page')
        context['page_range'] = self.get_host_data().get('page_range')
        context['paginator'] = self.get_host_data().get('paginator')
        context['username'] = self.get_object().username
        context['item'] = 'Article'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class VisitFileView(VisitArticleView):
    template_name = "home/center_for_visitor.html"

    def get_host_data(self):  # 获取主人的资料
        file_list = models.File.objects.filter(author_id=self.get_object().id)
        page, paginator, page_range = self.get_page(file_list, 10)
        return locals()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['item'] = 'File'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class VisitLinkView(VisitArticleView):
    template_name = "home/center_for_visitor.html"

    def get_host_data(self):  # 获取主人的资料
        link_list = models.Link.objects.filter(author_id=self.get_object().id)
        page, paginator, page_range = self.get_page(link_list, 10)
        return locals()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['item'] = 'Link'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class VisitSearchArticleView(VisitArticleView):

    def get_host_data(self):  # 获取主人的资料
        self.articles = models.Article.objects.filter(author_id=self.get_object().id)
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            self.articles = models.Article.objects.filter(title__icontains=keyword)
        page, paginator, page_range = self.get_page(self.articles, 10)
        return locals()

    def get_context_data(self, **kwargs):  # 重写get_context_data方法
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_host_data().get('keyword')
        context['page'] = self.get_host_data().get('page')
        context['item'] = 'Article'
        return context


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class VisitSearchFileView(VisitSearchArticleView):

    def get_host_data(self):  # 获取主人的资料
        self.files = models.File.objects.filter(author_id=self.get_object().id)
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            self.files = models.File.objects.filter(name__icontains=keyword)
        page, paginator, page_range = self.get_page(self.files, 10)
        return locals()


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class VisitSearchLinkView(VisitSearchArticleView):

    def get_host_data(self):  # 获取主人的资料
        self.links = models.Article.objects.filter(author_id=self.get_object().id)
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            self.links = models.Link.objects.filter(name__icontains=keyword)
        page, paginator, page_range = self.get_page(self.links, 10)
        return locals()


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class SearchView(CategoryView):
    # 模板位置
    template_name = 'main/search.html'

    def get_queryset(self):  # 重写get_queryset方法
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            articles = models.Article.objects.filter(title__icontains=keyword)  # 加i不区分大小写
            page, paginator, page_range = self.get_page(articles, 8)
            return locals()
        return locals()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_queryset().get('keyword')
        return context


class FileListView(CategoryView):
    # 模板位置
    template_name = 'main/file_list.html'

    def get_queryset(self):  # 重写get_queryset方法
        file_list = models.File.objects.filter()
        page, paginator, page_range = self.get_page(file_list, 20)
        return locals()


class LinkListView(CategoryView):
    # 模板位置
    template_name = 'main/link_list.html'

    def get_queryset(self):
        link_list = models.Link.objects.filter()
        page, paginator, page_range = self.get_page(link_list, 18)
        return locals()


class SearchFileListView(SearchView):
    # 模板位置
    template_name = 'main/file_list.html'

    def get_queryset(self):  # 重写get_queryset方法
        files = models.File.objects.all()
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            files = models.File.objects.filter(name__icontains=keyword)  # 加i不区分大小写
        page, paginator, page_range = self.get_page(files, 20)
        return locals()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_queryset().get('keyword')
        return context


class SearchLinkListView(SearchView):
    # 模板位置
    template_name = 'main/link_list.html'

    def get_queryset(self):  # 重写get_queryset方法
        links = models.Link.objects.all()
        keyword = self.request.GET.get('keyword')
        if keyword:  # 获取搜索的关键词
            links = models.Link.objects.filter(name__icontains=keyword)  # 加i不区分大小写
        page, paginator, page_range = self.get_page(links, 20)
        return locals()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_queryset().get('keyword')
        return context


def files(request):
    return HttpResponse("查看文件列表")


def links(request):
    return HttpResponse("查看链接列表")


def search(request):
    return HttpResponse("搜索文章/文件/链接")
