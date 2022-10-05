from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from login import models as login_models
from django.contrib.auth.models import User


class MainCategory(models.Model):
    # 主分类，例如Python基础学习，属于python主分类
    title = models.CharField(max_length=100, blank=True)
    # 分类的创建时间
    created = models.DateTimeField(default=timezone.now())
    # 创建人员
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')

    # admin站点信息 调试查看对象
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]


class SubCategory(models.Model):
    # 文章分类
    # 分类标题
    title = models.CharField(max_length=100, blank=True)
    # 分类的创建时间
    created = models.DateTimeField(default=timezone.now())
    # 主分类
    category = models.ForeignKey(
        MainCategory,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='category',
        default='1',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')

    # admin站点信息 调试查看对象
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        # db_table = 'tb_category'  # 修改表名
        # # verbose_name = '类别管理',
        # verbose_name_plural = verbose_name


# 博客文章
class Article(models.Model):
    # 文章作者。参数on_delete 用于指定数据删除的方式，避免两个关联表数据不一致
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
    # 文章标题
    title = models.CharField(max_length=100, blank=False)
    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', default='article/default.jpg',
                               verbose_name='avatar', blank=True)
    # upload_to指定图片上传的路径，不存在则自动创建
    # blank,设置为True时，字段可以为空。设置为False时，字段是必须填写的
    # 文章标签
    tag = models.CharField(max_length=200, blank=False)
    # 概要
    summary = models.CharField(max_length=200, blank=False)
    # 浏览次数
    views = models.PositiveIntegerField('views', default=0)
    # 文章正文
    body = MDTextField()
    created = models.DateTimeField('created', auto_now_add=True)  # 字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值
    # 文章更新时间 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)  # 字段保存时会自动保存当前时间，但要注意每次对其实例执行save()的时候都会将当前时间保存
    # 文章分类，使用外键
    category = models.ForeignKey(
        SubCategory,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='subcategory',
        default='1',
    )

    # 内部类class Meta用于给model定义元数据
    class Meta:
        # ’-created‘ 表明数据应该以倒叙排列
        ordering = ["-created"]   # 指定模型返回的数据的排列顺序
        # db_table = 'tb_article'
        # verbose_name = ''
        # verbose_name_plural = verbose_name
        # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
        # 它最常见的就是在Django管理后台中做为对象的显示值。因此应该总是为 __str__ 返回一个友好易读的字符串

    def __str__(self):
        # 将文章标题返回
        return self.title


# 文件模型
class File(models.Model):
    # 所关联的文章名称，利用文章名称作为外键
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default='2', blank=True)
    # 上传作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
    # 文件名称
    name = models.CharField(max_length=200)
    # 文件保存路径
    path = models.CharField(max_length=100)
    # 上传时间
    upload_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-upload_time"]


# 链接模型
class Link(models.Model):
    # 链接名
    name = models.CharField(max_length=200)
    # 链接地址
    url = models.URLField(max_length=200, default=None)
    # 上传作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
    # 上传时间
    upload_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # 将文章标题返回
        return self.name

    class Meta:
        ordering = ["-upload_time"]
