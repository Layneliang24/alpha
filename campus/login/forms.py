from django import forms
from captcha.fields import CaptchaField  # 图形验证码
from django.forms import widgets
from . import models


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': 'required'}))
    password = forms.CharField(label="Password", max_length=512,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label='Code', )  # 验证码图片和输入框是一个整体，无法设置样式！！！

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = models.User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError('Username not exist!')
        return username


class UserRegisterForm(forms.ModelForm):
    # 复写 User 的密码
    password = forms.CharField(label="Password", max_length=512,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    confirm_password = forms.CharField(label="Confirm Password", max_length=512,
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'form-control', 'placeholder': "Confirm Your Password"}))

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password', 'confirm_password')
        # fields = ('nickname', 'password', 'password2', 'portrait', 'phone', 'resume')
        # fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
        # exclude = None  # 排除的字段
        # labels = None  # 提示信息
        # help_texts = None  # 帮助提示信息
        widgets = {'username': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                   'email': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                   }  # 自定义插件
        # error_messages = None  # 自定义错误信息
        # error_messages用法：
        # error_messages = {
        #     'name': {'required': "用户名不能为空", },
        #     'age': {'required': "年龄不能为空", },
        # }

    # 对两次输入的密码是否一致进行检查, def clean_[字段]这种写法Django会自动调用，来对单个字段的数据进行验证清洗。
    def clean_confirm_password(self):
        data = self.cleaned_data
        if data.get('password') == data.get('confirm_password'):
            return data.get('password')
        else:
            raise forms.ValidationError("Passwords not same!")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Your username must be at least 3 characters long")
        elif len(username) > 20:
            raise forms.ValidationError("Your username is too long")
        else:
            filter_result = models.User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('Your username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        filter_result = models.User.objects.filter(email__exact=email)
        if len(filter_result) > 0:
            raise forms.ValidationError("Your email already exists")
        return email
