from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . import forms
from . import models


def empty(request):
    return redirect('/main/')


def confirm(request):
    return HttpResponse("用户确认页面")


class GetMethodMixin:
    form_class = forms.UserLoginForm
    template_name = 'login/login.html'
    initial = {'key': 'value'}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        # 已登录用户不能再次登录
        if request.user.id:
            return redirect("main:indexview")
        return render(request, self.template_name, locals())


@method_decorator(csrf_exempt, name="post")  # 装饰器name参数指明要装饰的函数名称
class LoginView(View, GetMethodMixin):  # 命名规范化，可继承复用
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():  # 判断数据是否合法，True合法
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            data = form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # if not user.has_confirmed:
                #     message = '该用户还未经过邮件确认！'
                #     return render(request, self.template_name, locals())
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("main:indexview")       # 这里也可以使用url反查
            else:
                message = 'Username or password error!'
                return render(request, self.template_name, locals())
        else:
            bad_message = "Opts! something wrong"
            return render(request, self.template_name, locals())


class RegisterView(View, GetMethodMixin):  # 继承混入类，可重用一些方法
    form_class = forms.UserRegisterForm         # 重写表单
    template_name = 'login/register.html'       # 重写模板位置
    initial = {'key': 'value'}

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            # new_user = form.save(commit=False)
            # #设置密码
            # new_user.set_password(form.cleaned_data['password'])
            # 将新用户保存到数据库中
            # new_user.save()   # 如果直接使用objects.create()方法后不需要使用save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['confirm_password']
            new_user = models.User.objects.create_user(username=username, password=password, email=email)
            user_profile = models.Profile(user=new_user)
            user_profile.save()
            good_message = "Congratulations, registration success! please go back and login!"
            return render(request, self.template_name, locals())
        else:
            bad_message = "Opts! something wrong"
            return render(request, self.template_name, locals())
