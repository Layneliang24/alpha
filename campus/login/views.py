from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import forms
from . import models
import hashlib
import datetime


def empty(request):
    return redirect('/login/login')


def logout(request):
    return redirect('/login/')


def confirm(request):
    return HttpResponse("用户确认页面")


class Login(View):
    form = forms.UserForm()
    template_name = 'login/login.html'

    @staticmethod
    def hash_password(password, salt='layneweb'):
        h = hashlib.md5()
        password += salt
        h.update(password.encode())  # update方法只接收bytes类型
        return h.hexdigest()

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        form = forms.UserForm(request.POST)
        if form.is_valid():  # 判断数据是否合法，True合法
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(name=username)
                # user = authenticate(username=username, password=password)  # +
                # auth_login(request, user)  # 保存登录会话,将登陆的信息封装到request.user,包括session  # +
            except:
                message = '用户不存在！'
                return render(request, self.template_name, locals())

            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return render(request, self.template_name, locals())

            if user.password == self.hash_password(password):  # 对比的是哈希值，用数据库里的哈希值和输入的哈希值对比
                print(username, password)
                request.session['is_login'] = True  # 新增session保存操作，记录用户状态
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                print('当前登录用户：' + request.session['user_name'])
                user.is_login = True
                user.save()
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, self.template_name, locals())
        else:
            return render(request, self.template_name, locals())


class Register(View):
    form = forms.RegisterForm

    @staticmethod
    def get(request):
        return HttpResponse("访问注册页面")
