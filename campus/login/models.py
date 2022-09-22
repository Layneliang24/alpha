from django.db import models
from django.contrib.auth.models import User


# 用户扩展信息
class Profile(models.Model):
    # 先建一个元组存储性别
    gender_type = (('male', '男'), ('female', '女'))
    # 与 User 模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 性别
    gender = models.CharField(max_length=32, choices=gender_type, default="女")
    # 昵称，可选
    nickname = models.CharField(max_length=191, blank=True)
    # 电话号码字段，必填
    phone = models.CharField(max_length=20, blank=False)
    # 头像，可选，需要设置默认头像
    portrait = models.ImageField(upload_to='portrait/%Y%m%d/', blank=True)
    # 个人简介，可选
    resume = models.TextField(max_length=500, blank=True)
    # 是否已经邮件确认
    has_confirmed = models.BooleanField(default=False)
    # 创建时间
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'user {}'.format(self.user.name)     # 这里与参考不一样

    class Meta:  # 元数据里定义用户按创建时间的反序排列，也就是最近的最先显示；尚未搞明白
        ordering = ["-c_time"]
        verbose_name = "user"
        verbose_name_plural = "users"


class ConfirmString(models.Model):  # 创建新的表格来装数据
    code = models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)    # 字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "confirm code"
        verbose_name_plural = "confirm codes"
