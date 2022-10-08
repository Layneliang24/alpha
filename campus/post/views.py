from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.views import View
from main import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import os


def empty(request):
    return redirect('post:article')


def post(request):
    pass


@method_decorator(login_required(login_url="login:login"), name='dispatch')
class PostArticleView(View):
    form_class = forms.PostArticleForm  # 重写表单
    template_name = 'post/article.html'  # 重写模板位置
    initial = {'key': 'value'}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, locals())

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # 同名文章判断
            same_title_article = models.Article.objects.filter(title=form.cleaned_data.get('title'))
            if same_title_article:
                bad_message = 'Oops, The title of this article already exists!'
                return render(request, 'post/article.html', locals())
            new_article = models.Article()
            new_article.author = User.objects.get(id=request.user.id)
            new_article.title = form.cleaned_data.get('title')  # 对新文章赋值。
            if form.cleaned_data.get('avatar'):
                new_article.avatar = form.cleaned_data.get('avatar')
            new_article.tag = form.cleaned_data.get('tag')
            new_article.summary = form.cleaned_data.get('summary')  # 单词错误
            new_article.category = form.cleaned_data.get('category')
            new_article.body = form.cleaned_data.get('body')
            # 新的文章，需要先保存，才可以被文件引用为外键。
            new_article.save()
            # 遍历写入到数据库中
            for f in request.FILES.getlist('file'):
                # 写入到数据库中
                file_model = models.File(article=new_article, name=f.name,
                                         path=os.path.join('./media/upload', f.name))
                file_model.save()

                # 写入到服务器本地
                destination = open(os.path.join("./media/upload", f.name), 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            good_message = 'Post success! well done, Keep on the good work!'
            return render(request, self.template_name, locals())
        else:
            bad_message = "Opts! something wrong"
            return render(request, self.template_name, locals())


def file(request):
    return HttpResponse("发布文件")


def link(request):
    return HttpResponse("发布链接")
