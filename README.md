# Django教程之个人博客网站-优化版

## 友情链接

[杜赛说编程（变态详细）（本教程）](https://www.dusaiphoto.com/article/71/)

[ProcessOn（本教程组织架构）](https://www.processon.com/mindmap/63280aca7d9c081f94dbaf43)

[Bootstrap4中文网](https://www.fengjinwei.com/tool/bootstrap4/pages/components.html)

[Layui|前端框架模板](http://layui.sandbean.com/demo/index.htm)

[Django文档|英文，非常详细](https://www.djangoproject.com/)

[Django中文网|各种教程/详细](https://www.django.cn/article/)

[Font awesome中文网](http://www.fontawesome.com.cn/faicons/)

## 重要基础知识

1. ==CSS要防止溢出的话，设置overflow: auto只对块级元素\<div>生效==
2. ==CSS不换行写法：display:inline==
3. url匹配从上至下，像下面这种事设计的话，应该加上$结尾，避免所有的匹配都给了最短那个url

```python
re_path('^center$', views.CenterView.as_view(), name='center'),
re_path('^center/file', views.CenterFileView.as_view(), name='file'),
re_path('^center/link', views.CenterLinkView.as_view(), name='link'),
re_path('^center/profile', views.profile, name='profile'),
```

4. 如何将user传到视图里去？[参考](https://blog.csdn.net/tmpbook/article/details/43191177)

```python
# 参考：https://blog.csdn.net/tmpbook/article/details/43191177, 如何将user传到类视图
# def get_form_kwargs(self):
#     kwargs = super(ProfileUpdateView, self).get_form_kwargs()
#     kwargs.update({
#         'user': self.request.user
#     })
#     return kwargs
```







## 一、优化项

- [x] **明确项目框架，设计各种页面，添加个人主页界面（简历，经历）、学习园地**

[ProcessOn](https://www.processon.com/mindmap/63280aca7d9c081f94dbaf43)

![个人网站](C:/Typora%20picture%20sharing/%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99-166357975174010.png)

- [x] **充分利用Django提供的各种便捷方法，减少代码冗余，减少代码量，使代码整洁。**
- 使用类视图等
- 使用django自带的用户管理系统，可拓展
- 删除模板中硬编码的URLs，使用{% url xxx:xxx %}[参考](https://www.liujiangblog.com/course/django/89)
- 模型表单modelform，字段等。
- 使用快捷方式：get_object_or_404()
- [x] **目录结构，URL结构，名称，模型字段，规范要求。**
- 目录结构，
- [x] **CSS嵌入方式，改为链接式，将 HTML 文档和 CSS 文件完全分离**
- [x] **充分使用Githup保存修改记录，实现版本控制。**
- [x] **Bootstrp4引用方式修改为本地，加快加载速度。**
- [x] **使用虚拟环境**
- [ ] **结合使用Nginx**
- [ ] *采用前后端分离的形式*

==什么是前后端分离==

**传统的开发协作模式**一般是这样的：

* 前端写好静态的HTML页面交付给后端开发。
* 后端使用模板引擎去套模板，同时内嵌模板变量和逻辑。
* 前后端集成对接，遇到问题前台后台都返工。
* 集成调试，直至成功。

这种模式的**问题**在于：

* 前端调试要安装完整的后端开发工具，并且遇到问题需要后端开发帮忙调试。
* 前后端耦合，甚至还要求后端人员会 Javascript 等前端语言。
* 前端页面里嵌入后端的代码，一旦后端换了语言，简直就要重做。

对于大项目来说，这样的模式增加了沟通成本，前后端的开发进度相互影响，从而降低了开发效率。

而在**前后端分离模式**下，前端和后端只通过简单的接口（API）进行数据交流，而不用像模板将数据藏在某个 div 里。前后端工程师约定好数据接口，并行开发互不影响。即使其中一方的需求发生变更，只要接口不变，对方就不需要更改代码。

前后端分离模式摆脱了笨重的模板引擎，是当前 web 开发的大趋势之一，花时间学了绝对不亏。

- [ ] **使用Django信号系统**

- [ ] **新玩法，生成PDF/CSV文件**[参考|刘江的博客教程](https://www.liujiangblog.com/course/django/143)
- [ ] **添加测试功能**
- [ ] **自定义后台管理**
- [ ] **实现重置用户密码**
- [ ] **CSS添加格式化代码**
- [x] **实现博主空间功能**



## 二、使用虚拟环境

**虚拟环境（virtualenv，或venv ）**是 Python 多版本管理的利器，可以使每个项目环境与其他项目独立开来，保持环境的干净，解决包冲突问题。你可以将虚拟环境理解为一个隔绝的小系统。

**从Python3.3版本开始就自带了虚拟环境，不需要安装，配置一下就可以用了。**

新建一个文件夹，本教程中为`alpha`。进入此文件夹：

```powershell
C:\WINDOWS\system32>cd C://alpha
C:\alpha>
```

输入配置venv的命令，其中的`env`为虚拟环境的放置目录：

```powershell
C:\alpha>python -m venv env
```

创建完成后，==输入env\Scripts\activate.bat，即可进入虚拟环境==：

```powershell
(env) C:\alpha>
```

**盘符前有`(env)`标识说明进入venv成功。**

**在虚拟环境下**，输入命令`pip install django==4.0.4`安装django：

```powershell
(env) C:\alpha>pip install django==4.0.4
Collecting django==4.0.4
  Downloading Django-4.0.4-py3-none-any.whl (8.0 MB)
     ---------------------------------------- 8.0/8.0 MB 2.1 MB/s eta 0:00:00
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting tzdata
  Downloading tzdata-2022.2-py2.py3-none-any.whl (336 kB)
     ---------------------------------------- 336.4/336.4 KB 2.3 MB/s eta 0:00:00
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     ---------------------------------------- 42.3/42.3 KB 682.3 kB/s eta 0:00:00
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.2 django-4.0.4 sqlparse-0.4.2 tzdata-2022.2
```

还是在虚拟环境下，在alpha目录中创建alpha项目：(==Django的一切操作都要在虚拟环境下进行==)

```powershell
(env) C:\alpha>django-admin startproject alpha
```

此时的目录结构：

```powershell
(env) C:\alpha>tree alpha
卷 Local Disk 的文件夹 PATH 列表
卷序列号为 AA17-54D9
C:\ALPHA\ALPHA
└─alpha
```

运行项目：

```powershell
(env) C:\alpha\alpha>python manage.py runserver 8002
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 20, 2022 - 21:52:37
Django version 4.0.4, using settings 'alpha.settings'
Starting development server at http://127.0.0.1:8002/
Quit the server with CTRL-BREAK.
```

![image-20220920215413105](C:/Typora%20picture%20sharing/image-20220920215413105.png)

## 三、创建apps并设置项目目录

### 1.全局设置

```python
# 将apps文件夹加入到pythonpath中，以被python识别该目录下的app
sys.path.insert(0, os.path.join(BASE_DIR, 'campus'))
```

本项目分为两个部分：

- 第一部分是introduction，主要是个人的经历和简历链接（面试的时候使用）
- 第二部分是学习园地campus（可改造成FAQ平台），里面包含四个app，login、main、post、home。

本文项目主目录如下：

```powershell
C:\ALPHA\ALPHA
├─alpha
│  └─__pycache__
├─campus
│  ├─home
│  │  └─migrations
│  ├─login
│  │  └─migrations
│  ├─main
│  │  └─migrations
│  └─post
│      └─migrations
├─introduction
│  └─migrations
├─media
├─static
└─templates
```

注册app------略

## 四、使用GitHub管理

### 1.在Git Bash里面把`C:\alpha\alpha`目录变成Git可以管理的仓库  

```powershell
ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha
$ git init
Initialized empty Git repository in C:/alpha/alpha/.git/
```

### 2.github网站创建仓库`alpha`

![image-20220921121541039](C:/Typora%20picture%20sharing/image-20220921121541039.png)

### 3.把文件添加到版本库  (先本后远)

```powershell
git add '*'
```

### 4.把本地仓库与远程仓库关联(先本后远)

```powershell
ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha (master)
$ git remote add origin git@github.com:Layneliang24/alpha.git
```

### 5.从远程仓库克隆（先远后本）

```powershell
ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha
$ git clone git@github.com:Layneliang24/alpha.git
Cloning into 'alpha'...
remote: Enumerating objects: 34, done.
remote: Counting objects: 100% (34/34), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 34 (delta 11), reused 31 (delta 11), pack-reused 0
Receiving objects: 100% (34/34), 6.33 KiB | 2.11 MiB/s, done.
Resolving deltas: 100% (11/11), done.
```

### 6.从本地推送更新到远程仓库

```powershell
Layne@layne MINGW64 /c/alpha/alpha (master)
$ git add '*'

Layne@layne MINGW64 /c/alpha/alpha (master)
$ git commit -m 'settings.py完成数据库设置'
[master 0aadceb] settings.py完成数据库设置
 1 file changed, 6 insertions(+), 20 deletions(-)

Layne@layne MINGW64 /c/alpha/alpha (master)
$ git push origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 680 bytes | 340.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To github.com:Layneliang24/alpha.git
   e7ad4aa..0aadceb  master -> master
```

### 7.从远程仓库==拉取==更新

[Git更新远程仓库代码到本地|参考](https://www.cnblogs.com/zhaijiahui/p/9006816.html)

```powershell
$ git status			# 检查本地是否有未提交的修改，
$ git pull
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 6), reused 5 (delta 3), pack-reused 0
Unpacking objects: 100% (8/8), 1015 bytes | 2
......
```

**【git 使用】【git常见错误处理一】状态不一致：Your branch is ahead of 'origin/master' by 2 commits**

如果保证git server上确实已经提交了代码，仅仅只是本地git状态不一致，则可以用以下命令：

```powershell
 git fetch - -all
 git pull
 git reset - -hard origin/master
```

然后查看状态，正确了。

```powershell
ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha (master)
$ git fetch --all

ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha (master)
$ git pull
Already up to date.

ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha (master)
$  git reset --hard origin/master
HEAD is now at 7836f22 settings.py完成主要apps的注册

ZKTeco@DESKTOP-BODCV28 MINGW64 /c/alpha/alpha (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

### 8.删除已提交commit

[参考|Git: 删除commit记录方法(删除push失败的记录)](https://blog.csdn.net/quiet_girl/article/details/79487966)

- `git reset --hard HEAD^`因为你要撤销最新的一个 commit，所以你需要恢复到它的父 commit ，也就是 `HEAD^`。那么在这行之后，你要丢弃的最新一条就被撤销了：

![image-20221013234012547](C:/Typora%20picture%20sharing/image-20221013234012547.png)

```bash
Layne@layne MINGW64 /c/alpha/alpha (master)
$ git commit -m '完成所有功能'
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

Layne@layne MINGW64 /c/alpha/alpha (master)
$ git log
commit 74e469e0209222aebeabf3c487be4d3814128b0c (HEAD -> master)
Author: Layneliang24 <2227208441@qq.com>
Date:   Thu Oct 13 23:20:36 2022 +0800

    完成所有功能设计

commit d825f6b0fce3d90a3109c93f3a486efcb46f61f8
Author: Layneliang24 <2227208441@qq.com>
Date:   Thu Oct 13 23:00:30 2022 +0800

    完成所有功能

commit ed7b9ced43ea2fa44d933219a535cf0842fd8ac7
Author: Layneliang24 <2227208441@qq.com>
Date:   Thu Oct 13 22:44:41 2022 +0800

    完成所有设计

commit a1c74b8519503a95bf1541351235183866f35876 (origin/master)
Author: Layneliang24 <2227208441@qq.com>
Date:   Sun Oct 9 00:35:17 2022 +0800

    完成用户主页设计

Layne@layne MINGW64 /c/alpha/alpha (master)
$ git reset --hard HEAD^
Updating files: 100% (7/7), done.
HEAD is now at d825f6b 完成所有功能

Layne@layne MINGW64 /c/alpha/alpha (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

Layne@layne MINGW64 /c/alpha/alpha (master)
```



## 五、设置数据库、编写模型

### 1.cmd下直接创建数据库 

```powershell
(env) C:\alpha>mysql -u root -p
Enter password: *********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2163
Server version: 8.0.29 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE alpha;
Query OK, 1 row affected (0.04 sec)
```

### 2.在settings文件里面配置数据库：  

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 使用 mysql 数据库管理系统
        'NAME': 'alpha',  # 刚刚创建的数据库名称
        'USER': 'root',  # 连接数据库的用户名
        'PASSWORD': 'meimei520',  # root 用户对应的密码
        'HOST': '',  # 主机地址，不填写的话，默认为 127.0.0.1
        'PORT': '',  # 连接 mysql 的端口，不填写的话，默认为 3306
    }
}
```

### 3.编写Model模型：  

#### ==A.用户资料模型Profile==：

[参考|Django搭建个人博客：扩展用户信息](https://www.dusaiphoto.com/article/37/)

基于django自带的用户模型User进行拓展，添加诸如电话号码，昵称，用户头像等。扩展User模型又有不同的方法。在大多数情况下，使用**模型一对一链接**的方法是比较适合的。

`login/models.py  `

```python
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
```

- 每个`Profile`模型对应唯一的一个`User`模型，形成了对User的外接扩展，因此你可以在`Profile`添加任何想要的字段。

* 内部类`Meta`中的`ordering`定义了数据的排列方式。`-created`表示将以创建时间的倒序排列，保证了最新的文章总是在网页的最上方。
* `__str__`方法定义了需要表示数据时应该显示的名称。给模型增加 `__str__`方法是很重要的，它最常见的就是在Django管理后台中做为对象的显示值。因此应该总是返回一个友好易读的字符串。

>内部类`class Meta`提供模型的元数据。元数据是**“任何不是字段的东西”**，例如排序选项`ordering`、数据库表名`db_table`、单数和复数名称`verbose_name`和 `verbose_name_plural`。这些信息不是某篇文章私有的数据，而是整张表的共同行为。
>
>要不要写内部类是完全可选的，当然有了它可以帮助理解并规范类的行为。

修改view，使得`Profile`表根据是否已经存在而动态的创建、获取：

```

```

#### B.用户确认码模型ConfirmString：

用来存储用户的确认码，注册验证使用。

`login/models.py  `

```python
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
```

#### C.文章主分类模型MainCategory：

用来定义文章的主分类，例如`Django教程之个人博客网站`的主分类是django。

`main/models.py  `

```python
class MotherCategory(models.Model):
    # 分类的母分类，例如Python基础学习，属于python母分类
    title = models.CharField(max_length=100, blank=True)
    # 分类的创建时间
    created = models.DateTimeField(default=timezone.now())

    # admin站点信息 调试查看对象
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
```

#### D.文章子分类模型SubCategory：

用来定义文章的子分类，例如`Django教程之个人博客网站`。

`main/models.py  `

```python
class SubCategory(models.Model):
    # 文章分类
    # 分类标题
    title = models.CharField(max_length=100, blank=True)
    # 分类的创建时间
    created = models.DateTimeField(default=timezone.now())
    # 主分类
    maincategory = models.ForeignKey(
        MainCategory,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='maincategory',
        default='1',
    )

    # admin站点信息 调试查看对象
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        # db_table = 'tb_category'  # 修改表名
        # # verbose_name = '类别管理',
        # verbose_name_plural = verbose_name
```

#### E.文章模型Article：

所有的文章。

这里就需要安装`mdeditor`和`markdown`

```python
(env) C:\alpha\alpha>pip install django-mdeditor	# 用于后台编辑
(env) C:\alpha\alpha>pip install markdown			# 用于前端显示
```

`main/models.py`

```python
# 博客文章
class Article(models.Model):
    # 文章作者。参数on_delete 用于指定数据删除的方式，避免两个关联表数据不一致
    author = models.ForeignKey(login_models.Profile, on_delete=models.CASCADE, default='layne')
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
```

#### F.文件模型File：

所有的文件。

`main/models.py`

```python
# 文件模型
class File(models.Model):
    # 所关联的文章名称，利用文章名称作为外键
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default='2', blank=True)
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
```

#### G.链接模型Link：

所有的链接。

`main/models.py`

```python
# 链接模型
class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, default=None)
    # 上传时间
    upload_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # 将文章标题返回
        return self.name
    
    class Meta:
        ordering = ["-upload_time"]
```

### 4.重建数据库

在虚拟环境下安装`mysqlclient`

```python
(env) C:\alpha\alpha>pip install mysqlclient
Collecting mysqlclient
  Downloading mysqlclient-2.1.1-cp310-cp310-win_amd64.whl (178 kB)
     ---------------------------------------- 178.4/178.4 kB 1.8 MB/s eta 0:00:00
Installing collected packages: mysqlclient
Successfully installed mysqlclient-2.1.1
```

前面讲过，每次改动模型后都需要进行数据的迁移。由于`portrait`字段为图像字段，需要安装第三方库`Pillow`来支持：

```powershell
(env) C:\alpha>pip install Pillow
Collecting Pillow
  Downloading Pillow-9.2.0-cp310-cp310-win_amd64.whl (3.3 MB)
     ---------------------------------------- 3.3/3.3 MB 5.4 MB/s eta 0:00:00
Installing collected packages: Pillow
Successfully installed Pillow-9.2.0
```

安装成功后，通过`makemigrations`、`migrate`迁移数据：

```python
(env) C:\alpha\alpha>python manage.py makemigrations
Migrations for 'login':
  campus\login\migrations\0001_initial.py
    - Create model Profile
    - Create model ConfirmString

(env) C:\alpha\alpha>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, login, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
......
```

### 5.把模型注册到后台------==略==

## 六、URL路由设计

### 1.urls全局路由（总路由）设置

[参考|Django路由系统-URLconf配置、正则表达式简述](https://www.jianshu.com/p/a9381b765540)

`alpha/urls.py`

```python
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('captcha/', include('captcha.urls')),  # 图形验证码功能。要在主项目下添加。
                  re_path(r'mdeditor/', include('mdeditor.urls')),  # 为实现markdown功能，不清楚有啥异常
                  re_path(r'^login/', include(('login.urls', 'login'), namespace='login')),  # 将路由分发给下面的app处理
                  re_path(r'^home/', include(('home.urls', 'home'), namespace='home')),
                  re_path(r'^post/', include(('post.urls', 'post'), namespace='post')),
                  re_path(r'^main/', include(('main.urls', 'main'), namespace='main')),
                  re_path(r'^introduction/', include(('introduction.urls', 'introduction'), namespace='introduction')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 加上这句至关重要，不然照片不显示

if settings.DEBUG:  # 添加媒体文件url,生产环境下使用
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```

path为Django的路由语法：

- 参数`login/`分配了app的访问路径；
- `include`将路径分发给下一步处理；
- ==`namespace`可以保证反查到唯一的url，即使不同的app使用了相同的url（后面会用到）。==
- 匹配模式的最开头不需要添加/，因为==默认情况下，每个url都带一个最前面的/==，既然大家都有的部分，就不用浪费时间特别写一个了。

### 2.app路由设置

#### A.Login

`login/urls.py`

```python
from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'login'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^login', views.Login.as_view()),
    re_path('^register', views.register),
    re_path('^logout', views.logout),
    re_path('^confirm', views.confirm),
]
```

#### B.Main

`main/urls.py`

```python
from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'main'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^index', views.index),
    re_path('^categories', views.categories),
    re_path('^articles', views.articles),
    re_path('^files', views.files),
    re_path('^links', views.links),
    re_path('^search', views.search),
]
```

#### C.Post

`post/urls.py`

```python
from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'post'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^post', views.post),
    re_path('^article', views.article),
    re_path('^file', views.file),
    re_path('^link', views.link),
]
```

#### D.Home

`home/urls.py`

```python
from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'home'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^profile', views.profile),
    re_path('^edit', views.edit),
    re_path('^articles', views.articles),
    re_path('^files', views.files),
    re_path('^links', views.links),
    re_path('^reset', views.reset),
]
```

#### E.Introduction

`introduction/urls.py`

```python
from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'introduction'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^index', views.index),
    re_path('^post', views.post),
    re_path('^edit', views.edit),
    re_path('^resume', views.resume),
]
```

## 七、视图和模板设计

### 1.settings全局设置（模板路径）

我先得把模板的位置告诉django，因此需要编辑 settings.py 文件的 'DIRS'
`alpha/settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 加入这个之后，调用图片路径时可以使用{{ MEDIA_URL }}{{ object.img }}的方式拼接图片路径。
                'django.template.context_processors.media',     # +
            ],
        },
    },
]
```

也要设置静态文件加载路径

`alpha/settings.py`

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
```

为了避免“Forbidden (403) CSRF verification failed. Request aborted.“错误，可以把以下的csrf注释掉：

```

```

本文采用另一种更好的方法：[Django中关于“CSRF verification failed”的问题](https://www.cnblogs.com/iwatson/p/13932258.html)

### 2.视图设计

#### A.==使用类视图==

##### a.类视图的简介

[参考|Django 官方推荐的姿势：类视图](https://zhuanlan.zhihu.com/p/88409906)

[参考（简书，非常详细）|【Django】基于类的视图](https://www.jianshu.com/p/e0663799b091)

[参考|杜塞说编程](https://www.dusaiphoto.com/article/52/)

[刘江的博客教程也有](https://www.liujiangblog.com/course/django/279)

[参考|知乎](https://zhuanlan.zhihu.com/p/21372914?refer=djstudyteam)

[Django的ListView超详细用法(含分页paginate)](http://www.cppcns.com/jiaoben/python/313854.html)

以函数的方式定义的视图称为**函数视图**，函数视图便于理解。但是遇到一个视图对应的路径提供了多种不同HTTP请求方式的支持时，便需要在一个函数中编写不同的业务逻辑，代码可读性与复用性都不佳。

在Django中也可以使用类来定义一个视图，称为**类视图。**类视图的优点：代码可读性好、代码的复用性更高，如果其他地方需要用到类视图的某个特定逻辑，直接继承该类视图即可。

使用类视图可以将视图对应的不同请求方式以类中的不同请求方法来区别定义，如：

![image-20220923135531705](C:/Typora%20picture%20sharing/image-20220923135531705.png)

假设我们有一个[博客列表](https://www.dusaiphoto.com/article/detail/16/)，列表有一个GET方法，那么用视图函数看起来像这样：

```python
views.py

def article_list_example(request):
    """处理GET请求"""
    if request.method == 'GET':
        articles = ArticlePost.objects.all()
        context = {'articles': articles}
        return render(request, 'article/list.html', context)
```

而在**类视图**中，则变为这样：

```python
views.py

from django.views import View

class ArticleListView(View):
    """处理GET请求"""
    def get(self, request):
        articles = ArticlePost.objects.all()
        context = {'articles': articles}
        return render(request, 'article/list.html', context)
```

从本质上讲，基于类的视图允许你使用不同的**类实例方法**（即上面的`def get()`）响应不同的HTTP请求方法，而不需要使用**条件分支**代码。这样做的好处是把不同的HTTP请求都分离到独立的函数中，逻辑更加清晰，并且方便复用。

**需要注意的是**，因为Django的URL解析器希望将请求发送到**函数**而不是类，所以类视图有一个 `as_view()`方法，该方法返回一个函数，当请求匹配关联模式的URL时，则调用该函数。

即，视图函数的url原本写为：

```python
urls.py

...
urlpatterns = [
    path('...', views.article_list_example, name='...'),
]
```

**类视图的url需改写为：**

```python
urls.py

...
urlpatterns = [
    path('...', views.ArticleListView.as_view(), name='...'),
]
```

##### b.==使用内置的通用视图==

像**列表**这样的功能在web开发中是很常见的，开发者会一遍又一遍写几乎相同的列表逻辑。Django的**通用视图**正是为缓解这种痛苦而开发的。它们对常用模式进行抽象，以便你快速编写公共视图，而无需编写太多代码。

因此用列表通用视图改写如下：

```python
views.py

from django.views.generic import ListView

class ArticleListView(ListView):
    # 上下文的名称
    context_object_name = 'articles'
    # 查询集
    queryset = ArticlePost.objects.all()
    # 模板位置
    template_name = 'article/list.html'
```

列表继承了父类`ListView`，也就获得了父类中的处理列表的方法，因此你可以看到，我们在自己的类中没有写任何处理的逻辑，仅仅是赋值了几个变量而已。

##### C.动态过滤

从数据库中筛选特定的内容也是常见的需求，类视图如何实现呢？

你可能想到了，将上面代码中改为`queryset = ArticlePost.objects.filter()`就可以了。

除此之外，**更好的办法**是覆写`get_queryset()`方法：

```python
views.py

...

class ArticleListView(ListView):
    context_object_name = 'articles'
    template_name = 'article/list.html'

    def get_queryset(self):
        """
        查询集
        """
        queryset = ArticlePost.objects.filter(title='Python')
        return queryset
```

例子中只是过滤出标题为“Python”的文章而已，有些大材小用了；但是你可以在`get_queryset()`中写复杂的联合查询逻辑，满足个性化的功能。

##### d.添加上下文

在博客列表的设计时，我们返回给模板的**上下文**除了`articles`以外，还有很多额外的信息，如`order`、`search`；在类视图中同样可以实现，改写`get_context_data()`方法即可：

```python
views.py

...

class ArticleListView(ListView):
    ...

    def get_context_data(self, **kwargs):
        # 获取原有的上下文
        context = super().get_context_data(**kwargs)
        # 增加新上下文
        context['order'] = 'total_views'
        return context
```

除此之外，`ListView`还有些别的方法可以覆写，深入了解可以看这里：[官方文档](https://docs.djangoproject.com/zh-hans/2.1/ref/class-based-views/generic-display/#listview)

##### e.混入类

**混入类（Mixin）**是指**具有某些功能、通常不独立使用、提供给其他类继承功能**的类。嗯，就是“混入”的字面意思。

前面的列表视图中已经有`get_context_data()`方法了。假设需要写一个功能类似的视频列表，就可以用**Mixin**来避免重复代码：

```python
views.py

...

class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = 'total_views'
        return context

class ArticleListView(ContextMixin, ListView):
    ...

class VideoListView(ContextMixin, ListView):
    ...
```

通过混入，两个子类都获得了`get_context_data()`方法。

> 从语法上看，混入是通过多重继承实现的。有区别的是，Mixin是**作为功能**添加到子类中的，而不是作为父类。

实际上Django内置了很多通用的Mixin类，实现了大部分常用的功能，点这里深入了解：[官方文档](https://docs.djangoproject.com/zh-hans/2.1/ref/class-based-views/mixins/)

##### f.详情页

既然列表都有通用视图，详情页当然也有对应的`DetailView`。

用类视图写一个[简单的详情页](https://www.dusaiphoto.com/article/detail/19/)：

```python
views.py

from django.views.generic import DetailView

class ArticleDetailView(DetailView):
    queryset = ArticlePost.objects.all()
    context_object_name = 'article'
    template_name = 'article/detail.html'
```

然后配置url：

```python
urls.py

...
urlpatterns = [
    # 详情类视图
    path('detail-view/<int:pk>/', views.ArticleDetailView.as_view(), name='...'),
]
```

注意这里传入的参数不是`id`而是`pk`，这是视图的要求（也可以传入`slug`）。`pk`是数据表的主键，在默认情况下其实就是`id`。

这就写好了！

也可以添加任何别的功能，比如[统计浏览量](https://www.dusaiphoto.com/article/detail/45/)：

```python
views.py

...
class ArticleDetailView(DetailView):
    ...
    def get_object(self):
        """
        获取需要展示的对象
        """
        # 首先调用父类的方法
        obj = super(ArticleDetailView, self).get_object()
        # 浏览量 +1
        obj.total_views += 1
        obj.save(update_fields=['total_views'])
        return obj
```

方法`get_object()`的作用是获取需要展示的对象。首先调用父类方法，将这个对象赋值给`obj`变量，然后再对其进行统计浏览量的操作，最后将对象返回。相当于在原有的方法中把自己的逻辑“塞”了进去。

关于`DetailView`更多特性看这里：[官方文档](https://docs.djangoproject.com/zh-hans/2.1/ref/class-based-views/generic-display/#detailview)

##### g.编辑

除了能够展示信息，通用视图还包含`CreateView`、`UpdateView`、`DeleteView`等**编辑**数据的类。

如果要[新建文章](https://www.dusaiphoto.com/article/detail/22/)，则视图可以这么写：

```python
views.py

from django.views.generic.edit import CreateView

class ArticleCreateView(CreateView):
    model = ArticlePost

    fields = '__all__'
    # 或者只填写部分字段，比如：
    # fields = ['title', 'content']

    template_name = 'article/create_by_class_view.html'
```

创建`create_by_class_view.html`文件（目录在哪，你应该已经很清楚了），写入：

```python
create_by_class_view.html

<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
```

最后添加url：

```python
urls.py

urlpatterns = [
    path('create-view/', views.ArticleCreateView.as_view(), name='...'),
]
```

虽然外观简陋（这不是重点），但现在这个视图确实已经能够创建新文章了！

##### h.TemplateView视图

在一个网站中，有一些页面不需要我们从数据库中提取数据到前端页面中，例如网址中的`“关于我们”` 这个页面一般都是在html中写死的数据，不需要进行改动，这个时候我们就可以直接在urls中直接渲染html文件，而不用视图函数或者视图类来进行渲染。

![image-20220925230544083](C:/Typora%20picture%20sharing/image-20220925230544083.png)

#### B.Login/views.py

使用类视图

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . import forms
from . import models


def empty(request):
    return redirect('/login/login')


def logout(request):
    return redirect('/login/')


def confirm(request):
    return HttpResponse("用户确认页面")


class GetMethodMixin:
    form_class = forms.UserLoginForm
    template_name = 'login/login.html'
    initial = {'key': 'value'}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, locals())


@method_decorator(csrf_exempt, name="post")  # 装饰器name参数指明要装饰的函数名称
class LoginView(View, GetMethodMixin):  # 命名规范化，可继承复用
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():  # 判断数据是否合法，True合法

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
                return redirect("main:index")       # 这里也可以使用url反查
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
```

> 注意：使用了类视图，之后，前面的路由设计URL也需要修改[跳转](#2.app路由设置)

- `authenticate()`方法验证用户名称和密码是否匹配，如果是，则将这个用户数据返回。
- `login()`方法实现用户登录，将用户数据保存在session中
- 当用户通过POST方法提交表单，我们先验证表单Form的数据是否有效。如果有效，我们先用Django User模型自带的 create_user方法创建user对象，再创建 user_profile。==用户通过一张表单提交数据，我们实际上分别存储在两张表里。==

#### C.Main/views.py(==可以使用django内置通用视类图==)

[（Django 学习小组：基于类的通用视图详解（一））|知乎](https://zhuanlan.zhihu.com/p/21372914?refer=djstudyteam)

[Django的ListView超详细用法(含分页paginate)](http://www.cppcns.com/jiaoben/python/313854.html)

```

```

- 解决报错“AttributeError: 'function' object has no attribute 'as_view'”  [给django视图类添加装饰器](https://www.cnblogs.com/Ting-light/p/10115584.html)

### 3.模板设计

设计思路：

`usebootstrap.html`为最基本模板, `login.html`、`register.html`、 `nav.html`都继承于`usebootstrap.html`，`footer.html`继承`nav.html`,  其他模板再继承`footer.html`

- `nav.html`展示导航栏
- footer.html展示导航栏,页码和页脚

继承的一些注意事项：

- 如果你在模版中使用 {% extends %} 标签，它必须是模版中的第一个标签。其他的任何情况下，模版继承都将无法工作。
- 在base模版中设置越多的 {% block %} 标签越好。请记住，子模版不必定义全部父模版中的blocks，所以，你可以在大多数blocks中填充合理的默认内容，然后，只定义你需要的那一个。多一点钩子总比少一点好。
- 如果你发现你自己在大量的模版中复制内容，那可能意味着你应该把内容移动到父模版中的一个 {% block %} 中。
- 为了更好的可读性，你也可以给你的{% endblock %} 标签一个 名字,在大型模版中，这个方法帮你清楚的看到哪一个　 {% block %} 标签被关闭了。 。例如：

```scss
{% block content %}
...
{% endblock content %}
```

- 不能在一个模版中定义多个相同名字的 block 标签。
- 继承模板的标签内容:{{ block.super }}

#### @Bootstrap引用模板usebootstrap.html

[使用Bootstrap4](https://blog.csdn.net/Hr_ving/article/details/120553585?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166399215816782388023771%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166399215816782388023771&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-120553585-null-null.142^v50^pc_rank_34_2,201^v3^add_ask&utm_term=bootstrap&spm=1018.2226.3001.4187)

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <title>
        {% block title %}
        usebootstrap
        {% endblock %}
    </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'bootstrap-4.4.1-dist/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'font-awesome-4.7.0/css/font-awesome.min.css' %}">
    <link href="{% static 'main/css/main.css' %}" rel="stylesheet"/>    <!--基础样式-->
    {% block link %}
    <!--自定义静态文件-->
    {% endblock link %}
</head>
<body>
<!--写入自定义内容-->

{% block nav %} {# 开放接口，且命名为content #}
<!--导航栏-->
{% endblock nav %}

{% block content %} {# 输入父模板的接口名字 #}
<!--页面主内容-->
{% endblock %}

{% block page %}
<!--分页-->
{% endblock page %}

{% block footer %}
<!--页脚-->
{% endblock footer %}

{% block script %}
<!--自定义脚本-->
{% endblock script %}

<!--自定义内容结束-->
<script src="{% static 'jquery/jquery-3.6.1.min.js' %}"></script>
<script src="https://cdn.staticfile.org/popper.js/1.15.0/umd/popper.min.js"></script>
<script src="{% static 'bootstrap-4.4.1-dist/js/bootstrap.min.js' %}"></script>
</body>
</html>
```

#### A.templates/login/login.html

```django
{% extends 'usebootstrap.html' %}
{% load static %}

{% block title %} Login {% endblock title %}

{% block link %}
<link href="{% static 'login/css/login.css' %}" rel="stylesheet"/>
{% endblock link %}

{% block content %}
<div class="container">
    <div class="col">
        <form class="form-login" action="{% url 'login:login' %}" method="post">
            {% if message %}
            <div class="alert alert-danger">{{ message }}</div>
            {% endif %}
            {% csrf_token %}
            <h3 class="text-center">Login</h3>
            {% for field in form %}
            <div class="form-group">
                {{ field.label_tag }}
                {{ field }}
                {% if field.errors %}
                <div class="alert alert-danger" style="margin: 10px;padding 5px;">{{ field.errors }}</div>
                {% endif %}
            </div>
            {% endfor %}
            <div id="button">
                <button type="submit" class="btn btn-primary" id="login-button">Login</button>
            </div>
            <br>
            <div class="text-center">Don't have an account?
                <a href="{% url 'login:register' %}" class="text-success">
                    <ins>Sign up</ins>
                </a>
            </div>
        </form>
    </div>
</div> <!-- /container -->
{% endblock content %}

{% block script %}
<script>
    $('img.captcha').attr("title", "点击更换验证码");
    $('img.captcha').click(function() {
        $.getJSON('/captcha/refresh/',function(json) {
            // This should update your captcha image src and captcha hidden input
            console.log(json);
            $("img.captcha").attr("src",json.image_url);
            $("#id_captcha_0").val(json.key);
        });
        return false;
    });
</script>
{% endblock script %}
```

说明：

- 使用了url反查`<a href="{% url 'login:register' %}" class="text-success">`

==login是总路由里设置的namespace, register是app路由里设置的name。==

-  有网页跳转就必加`{% csrf_token %}`

#### B.templates/login/register.html

```django
{% extends 'usebootstrap.html' %}
{% load static %}

{% block title %} Register {% endblock title %}

{% block link %}
<link href="{% static 'login/css/login.css' %}" rel="stylesheet"/>
{% endblock link %}

{% block content %}
<div class="container">
    <div class="col">
        <form class="form-login" action="{% url 'login:register' %}" method="post">
            {% if good_message %}
            <div class="alert alert-success">{{ good_message }}</div>
            {% elif bad_message%}
            <div class="alert alert-danger">{{ bad_message }}</div>
            {% endif %}
            {% csrf_token %}
            <h3 class="text-center">Welcome to Register!</h3>
            {% for field in form %}
            <div class="form-group">
                {{ field.label_tag }}
                {{ field }}
                {% if field.errors %}
                <div class="alert alert-danger" style="margin: 5px;padding 0px;">{{ field.errors }}</div>
                {% endif %}
            </div>
            {% endfor %}
            <div>
                <a href="{% url 'login:login' %}" class="text-success">
                    <ins>Back</ins>
                </a>
                <button type="submit" class="btn btn-primary" id="register-button">Register</button>
            </div>
        </form>
    </div>
</div>
{% endblock content %}
```

#### C.templates/main/nav.html(可以使用for循环优化)

##### a.个人信息下拉框设置

[参考|bootstrap页面头部用户图像下拉菜单](https://blog.csdn.net/cxzlp12345/article/details/82857022?locationNum=13&fps=1)

![image-20220929133457267](C:/Typora%20picture%20sharing/image-20220929133457267.png)

![image-20220929144841464](C:/Typora%20picture%20sharing/image-20220929144841464.png)

```django
{% extends 'usebootstrap.html' %}
{% load static %}

{% block title %} nav {% endblock title %}

{% block nav %}
<!--导航栏-->
<nav class="navbar navbar-expand-sm bg-dark navbar-dark" style="z-index: 1111"> <!--z-index设置模态框层级，不然被遮盖-->
    <a class="navbar-brand" href="{% url 'main:indexview' %}">HOME</a>
    <!-- 导航栏，文章分类部分-->
    <ul class="nav">
        {% for mcat in maincategory %}
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="" role="button" aria-haspopup="true"
               aria-expanded="false">{{ mcat.title }}</a>
            <div class="dropdown-menu">
                {% for scat in subcategory %}
                {% if scat.maincategory == mcat %}
                <a class="dropdown-item" href="{% url 'main:categoryview' %}">{{ scat.title }}</a>
                {% endif %}
                {% endfor %}
            </div>
        </li>
        {% endfor %}
    </ul>
    <div class="col order-last">
        <div id="search_tool">
            <!--搜索框-->
            <form class="form-inline my-2 my-lg-0" action="." method="get">
                <input class="form-control mr-sm-2" type="text" placeholder="Search" name="keyword"
                       aria-label="Search">
                <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
            </form>
        </div>
        <div class="dropdown layne-dropdown">
            <!--小头像照片-->
            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button"
               aria-haspopup="true" aria-expanded="false">
                <img class="rounded-circle layne-portrait-small" src="{{ profile.portrait.url }}" alt="None">
            </a>
            <!--用户下拉框-->
            <div class="dropdown-menu dropdown-menu-right" id="layne-dropdown-menu" aria-labelledby="dropdownMenuLink">
                <!--以容器形式展现-->
                <div style="margin-top: 10px;">
                    <div style="text-align: center;">
                        <img class="rounded-circle" src="{{ profile.portrait.url }}" alt="None"
                             style="width: 60px;height: 60px;">
                    </div>
                    <div style="text-align: center;line-height: 36px;font-size: 1.5rem;">
                        <span>{{ request.user.username }}</span>
                    </div>
                </div>
                <hr>
                <div style="display: flex;">
                    <div class="text-center layne-dropdown-menu-grid">
                        <i class="fa fa-pencil-square-o layne-fa" aria-hidden="true"></i>
                        <div class="text-center">my articles (1000)</div>
                    </div>
                    <div class="text-center layne-dropdown-menu-grid">
                        <i class="fa fa-file layne-fa" aria-hidden="true"></i>
                        <div class="text-center">my files</div>
                    </div>
                    <div class="text-center layne-dropdown-menu-grid">
                        <i class="fa fa-link layne-fa" aria-hidden="true"></i>
                        <div class="text-center">my links</div>
                    </div>
                </div>
                <div style="display: flex">
                    <div class="text-center layne-dropdown-menu-grid">
                        <i class="fa fa-user-circle layne-fa" aria-hidden="true"></i>
                        <div class="text-center">my profile</div>
                    </div>
                    <div class="text-center layne-dropdown-menu-grid">
                        <i class="fa fa-key layne-fa" aria-hidden="true"></i>
                        <div class="text-center">change pwd</div>
                    </div>
                    <div class="text-center layne-dropdown-menu-grid">
                        <a href="/admin/"><i class="fa fa-user-secret layne-fa" aria-hidden="true"></i></a>
                        <div class="text-center">management</div>
                    </div>
                </div>
                <div class="text-center">
                    <form action="{% url 'main:logout' %}">
                        <button type="button" class="border layne-dropdown-menu-exit btn btn-outline-danger"
                                data-toggle="modal" data-target="#exampleModalCenter">
                            <i class="fa fa-sign-out" style="color: black" aria-hidden="true"></i>
                            <b style="color: black">Exit</b>
                        </button>
                        <!-- Modal -->
                        <div class="modal" id="exampleModalCenter" tabindex="-1" role="dialog"
                             aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalCenterTitle">Info</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                            <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div class="modal-body">
                                        <b>Are you sure you want to quit ? </b>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-success" data-dismiss="modal">Stay</button>
                                        <form action="{% url 'main:logout' %}">
                                            <button type="submit" class="btn btn-danger">Quit</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</nav>
<!--内容接口-->
{% endblock nav %}
```

- ==这里的弹出模态框，需要设置`<nav>`元素的`z-index`属性。不然会被遮盖在底下==

##### b.效果：

![image-20220930230843004](C:/Typora%20picture%20sharing/image-20220930230843004.png)

#### D.templates/main/footer.html

```django
{% extends 'main/nav.html' %}

<!---------------------------页面标题----------------------------->

{% block title %}
footer
{% endblock title %}

<!----------------------------页面内容---------------------------->

{% block footer %} {# 输入父模板的接口名字 #}
<div class="footer mt-1 py-1 text-center">
    <div class="container">
        <span class="text-muted">Copyright @layne</span>
    </div>
</div>
{% endblock footer %}
```

#### E.templates/main/index.html

```django
{% extends 'main/footer.html' %}
{% load static %}

<!---------------------------页面标题----------------------------->

{% block title %}
Welcome to layneblog!
{% endblock %}

<!---------------------------静态资源----------------------------->

{% block link %}
<link href="{% static 'main/css/main-index.css' %}" rel="stylesheet"/>
{% endblock link %}

<!----------------------------页面内容---------------------------->


{% block content %} {# 输入父模板的接口名字 #}
<!-- content，文章列表部分 -->
<div class="map">
    <!--推荐栏目-->
    <div class="border border-primary card shadow recommend">
        <div class="card-header">
            <b>Recommends</b>
        </div>
        <div class="card-body card-body-recommend">
            {% for i in recommend %}
            <div class="card shadow bg-light border border-white card-small">
                <!--文章标题图-->
                <img class="card-img-top rounded" src="{{ i.avatar.url }}" alt="Card image cap">
                <!--文章文字内容-->
                <div class="card-bod card-body-small">
                    <!--文章标题-->
                    <div class="card-title card-title-recommend-small">
                        <a href="{% url 'main:articleview' i.id %}">{{ i.title }}</a>
                    </div>
                    <!--文章类目-->
                    <div class="article-category-recommend"><!--上下2，左右5-->
                        <a class="badge badge-info" href="{% url 'main:categoryview' %}/?category={{ i.category.id }}">
                            {{ i.category.title }}
                        </a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    <!--最近更新栏目-->
    <div class="border border-success card shadow latest">
        <div class="card-header">
            <b>Latest Uploads</b>
        </div>
        <div class="card-body card-body-latest">
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <!--活跃-->
                    <div class="carousel-item active">
                        <img class="d-block w-40 image-latest" src="{{ latest.0.avatar.url }}">
                        <div>
                            <div class="card-title-latest">
                                <a href="{% url 'main:articleview' latest.0.id %}">{{ latest.0.title }}</a>
                            </div>
                            <p class="card-text overflow-auto summary-latest">{{ latest.0.summary }}</p>
                        </div>
                        <!--文章类目-->
                        <div class="category-latest"><!--上下2，左右5-->
                            <a class="badge badge-info"
                               href="{% url 'main:categoryview' %}/?category={{ latest.0.category.id }}">
                                {{ latest.0.category.title }}
                            </a>
                        </div>
                    </div>
                    {% for i in latest %}
                    {% if forloop.first %}      {# 如果是第一个，那就跳过，避免重复 #}
                    {% else %}
                    <!--其他-->
                    <div class="carousel-item">
                        <img class="d-block w-40 image-latest" src="{{ i.avatar.url }}">
                        <div>
                            <div class="card-title-latest">
                                <a href="{% url 'main:articleview' i.id %}">{{ i.title }}</a>
                            </div>
                            <p class="card-text overflow-auto summary-latest">{{ i.summary }}</p>
                        </div>
                        <!--文章类目-->
                        <div class="category-latest"><!--上下2，左右5-->
                            <a class="badge badge-info"
                               href="{% url 'main:categoryview' %}/?category={{ i.category.id }}">
                                {{ i.category.title }}
                            </a>
                        </div>
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>
                <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>
    </div>
    <!--下载栏目-->
    <div class="border border-danger card shadow download">
        <div class="card-header">
            <div style="float: left"><b>Downloads</b></div>
            <div style="float: right">
                <a href="/download/" style="color: grey"><i class="fa fa-hand-o-right" aria-hidden="true"></i>
                    More>>></a>
            </div>
        </div>
        <div class="card-body">
            <ul class="list-group">
                {% for i in file_list %}
                <li class="list-group-item">
                    <div style="float: left">
                        {{ i.name }}
                    </div>
                    <div style="float: right">
                        <a href="/{{ i.path }}">[download]</a>
                    </div>
                </li>
                {% endfor %}
            </ul>
        </div>
    </div>
    <!--链接栏目-->
    <div class="border border-warning card shadow link">
        <div class="card-header">
            <div style="float: left"><b>Links</b></div>
            <div style="float: right">
                <a href="/link/" style="color: grey"><i class="fa fa-hand-o-right" aria-hidden="true"></i> More>>></a>
            </div>
        </div>
        <div class="card-body">
            {% for i in link_list %}
            <i style="margin-top: 5px;">
                <a href="{{ i.url }}">{{ i.name }}</a>
            </i><br/>
            {% endfor %}
        </div>
    </div>

</div>
<br>

{% endblock %}
```

#### F.templates/main/category.html

```django
{% extends 'main/footer.html' %}
{% load static %}

<!---------------------------页面标题----------------------------->

{% block title %}
Welcome to layneblog!
{% endblock %}

<!---------------------------静态资源----------------------------->


<!----------------------------页面内容---------------------------->

{% block content %} {# 输入父模板的接口名字 #}

<!-- content，文章列表部分 -->
<div class="container shadow-sm overflow-auto" style="width:75%;max-height: 665px;margin-top:20px;padding:5px 20px;">
    <!-- 列表循环 -->
    {% for article in page %}
    <!-- 文章内容 -->
    <div class="border border-light row shadow p-3 mb-5 bg-white rounded" style="position: sticky;top: 0;">
        <!-- 标题图 -->
        <div class="col-3">
            <img class="img-responsive"
                 src="{{ article.avatar.url }}"
                 alt="avatar" style="max-width:100%;max-height: 155px; border-radius: 20px">
        </div>
        <!--文字部分-->
        <div class="col">
            <!-- 栏目 -->
            <a role="button" href="#" class="btn btn-sm mb-2 btn-warning">{{ article.category.title }}</a>
            <!-- 标签 -->
            <span>
                        <a href="#" class="badge badge-secondary">{{ article.tag }}</a>
                </span>
            <!--标题-->
            <h4>
                <b><a href="/browse_articles/?cat_id={{ article.category.id }}&article_id={{ article.id }}"
                      style="color: black;">
                    {{ article.title }}</a></b>
            </h4>
            <!--摘要-->
            <div>
                <p style="color: gray;">
                    {{ article.summary }}
                </p>
            </div>
            <small><i class="fa fa-eye" style="color: green;margin-right: 5px"
                      aria-hidden="true"></i>浏览：{{ article.views }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <i class="fa fa-calendar" style="color: pink;margin-right: 5px"
                   aria-hidden="true"></i>创建日期：{{ article.created|date:"Y-m-d" }}</small>
        </div>
    </div>
    {% endfor %}
</div>

{% endblock %}

<!----------------------------页码---------------------------->

{% block page %}

<div class="container" style="width: 75%;padding:20px">
    <nav aria-label="Page navigation example">
        <ul class="pagination">
            <li class="page-item"><a class="page-link" href='?cat_id={{ cat_id }}&page=1'>First</a></li>
            {% if page.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?cat_id={{ cat_id }}&page={{ page.previous_page_number }}"
                   aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
            {% else %}
            {% endif %}
            {% for num in page_range %}
            {% if num == page.number %}
            <li class="page-item"><a class="page-link" href="#" style="color: red;">{{ num }}</a></li>
            {% elif num == "..." %}
            <li><i class="page-link">{{ num }}</i></li>
            {% else %}
            <li class="page-item"><a class="page-link" href="?cat_id={{ cat_id }}&page={{ num }}">{{ num }}</a></li>
            {% endif %}
            {% endfor %}
            {% if page.has_next %}
            <li class="page-item">
                <a class="page-link" href="?cat_id={{ cat_id }}&page={{ page.next_page_number }}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
            {% endif %}
            <li class="page-item"><a class="page-link"
                                     href="?cat_id={{ cat_id }}&page={{ paginator.num_pages }}">Last</a>
            </li>
        </ul>
    </nav>
</div>
{% endblock page %}
```

#### G.templates/main/article.html

##### a.处理DetailView第一个报错

![image-20221001085650687](C:/Typora%20picture%20sharing/image-20221001085650687.png)

设置url解决。

```python
path('^articles/<int:id>/', views.ArticleView.as_view(), name='articleview'),
```

```django
{% extends 'main/footer.html' %}
{% load static %}

<!---------------------------页面标题----------------------------->

{% block title %}
Welcome to layneblog!
{% endblock %}

<!---------------------------静态资源----------------------------->


<!----------------------------页面内容---------------------------->

{% block content %} {# 输入父模板的接口名字 #}

<!--文章全局-->
<div class="col-12"
     style="font-size: 18px;width: 90%;margin: 0 auto;padding-bottom: 0px;pxword-break: break-all;word-wrap: break-word;"
     xmlns="http://www.w3.org/1999/html">
    <!--width: 1000px;margin: 0 auto;让文章内容居中对齐-->
    {% if message %}
    <div class="alert alert-warning"><h3 style="margin: 0 auto;">{{ message }}</h3></div>
    {% else %}
    <!--文章定位-->
    <div class="rounded"
         style="margin-top: 20px;padding: 5px 0px;position:sticky;background-color: rgb(255 255 255 /0);">
        <em><i>{{ article.category.category.title }} > <a
                href="/browse_categories/?cat_id={{ article.category.id }}">
            {{ article.category.title }}</a> > <a
                href="/browse_articles/?cat_id={{ article.category.id }}&article_id={{ article.id }}">
            {{ article.title }}</a></i></em>
    </div>
    <!--文章正文-->
    <div style="width: 100%;display: grid;grid-template-columns: 19% 80%;grid-column-gap: 1%;">
        <!--目录栏-->
        <div class="pt-3 rounded"
             style="height: min-content;margin-top: 20px;float: left;position: sticky;top: 105px;">
            <p>Index: </p>
            <i style="font-size: 0.5rem;">{{ toc | safe }}</i>
        </div>
        <!--文章内容-->
        <div class="rounded" style="margin-top: 20px;">
            {{ article.body | safe }}
        </div>
        {% endif %}
    </div>
    <!--附件下载-->
    {% if files %}
    <div class="border border-success shadow p-5 mb-5 bg-white rounded">
        <h5>Downloads: </h5>
        <hr/>
        <ul>
            {% for file in files %}
            <li>
                <p style="margin: 2px;"><small>
                    {{ file.name }}
                    <a href="/{{ file.path }}">[click here to download]</a>
                </small></p>
            </li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}
    <hr>
    <small><i>Created: {{ article.created|date:"Y-m-d" }}</i></small><br>
    <small><i>Author: {{ article.author }}</i></small><br>
    <small><i>Browse: {{ article.views }}</i></small>
</div>

{% endblock %}

<!----------------------------页码---------------------------->

{% block page %}

<div style="width: 90%;padding: 5px 20px;margin: 0 auto;">
    <!--上一篇&下一篇-->
    <hr>
    <div>
        <div><b>Previous: </b>
            {% if previous_article %}
            <a href="/browse_articles/?article_id={{ previous_article.id }}">{{ previous_article }}</a>
            {% else %}
            None
            {% endif %}
        </div>
        <div><b>Next: </b>
            {% if next_article %}
            <a href="/browse_articles/?article_id={{ next_article.id }}">{{ next_article }}</a>
            {% else %}
            None
            {% endif %}
        </div>
    </div>
</div>

{% endblock page %}
```

#### H.templates/main/search.html

```django

```

#### I.templates/home/profile.html

##### a.用户资料修改页面参考

![image-20221006174038940](C:/Typora%20picture%20sharing/image-20221006174038940.png)

```django
{% extends 'usebootstrap.html' %}
{% load static %}

{% block title %} Edit Your Profile {% endblock title %}

{% block content %}
<div class="container">
    <div class="col">
        <form class="form-login" action="{% url 'home:profile' %}" enctype="multipart/form-data" method="post">
            <!--必须添加enctype="multipart/form-data"才可以上传照片，不然又排查半天！！！！！！！！！！！！-->
            {% if good_message %}
            <div class="alert alert-success">{{ good_message }}</div>
            {% elif bad_message%}
            <div class="alert alert-danger">{{ bad_message }}</div>
            {% endif %}
            {% csrf_token %}
            <h3 class="text-center">Complete your profile!</h3>
            <div class="form-group">
                <p>Username: </p>
                <b>{{ profile.user.username }}</b>
            </div>
            <div>
                {{ form.gender.label_tag }}
                <select class="form-control" name="gender">
                    <option>{{ profile.gender }}</option>
                    <option>female</option>
                    <option>male</option>
                </select>
            </div>
            <div class="form-group">
                {{ form.nickname.label_tag }}
                <input type="text" class="form-control" name="nickname" value="{{ profile.nickname }}">
            </div>
            <div class="form-group">
                {{ form.phone.label_tag }}
                <input type="text" class="form-control" name="phone" value="{{ profile.phone }}">
            </div>
            <div class="form-group">
                {{ form.resume.label_tag }}
                <textarea class="form-control" name="resume">{{ profile.resume }}</textarea>
                <!--name属性一定要和表单的字段一致，不然表单会无效，又排查半天！！！！！！-->
            </div>
            <div class="form-group">
                {{ form.portrait.label_tag }}<br/>
                <img class="rounded-circle" src="{{ profile.portrait.url }}" style="width: 200px;height: 200px"/>
                <div style="margin-top: 10px;">
                    <small>upload:</small>
                    <input type="file" name="portrait" accept="image/*">
                </div>
            </div>

            <div style="margin-top: 0px;">
                <a href="{% url 'login:login' %}" class="text-success">
                    <ins>Back</ins>
                </a>
                <button type="submit" class="btn btn-primary" style="margin-top: 10px;float: right;">Modify</button>
            </div>
        </form>
    </div>
</div>
{% endblock content %}

{% block footer %} {# 输入父模板的接口名字 #}
<div class="footer mt-1 py-1 text-center">
    <div class="container">
        <span class="text-muted"><i class="fa fa-copyright" aria-hidden="true"></i>Copyright @layne</span>
    </div>
</div>
{% endblock footer %}
```

- ==必须添加enctype="multipart/form-data"才可以上传照片，不然又排查半天！！！！！！！！！！！！==

- ==name属性一定要和表单的字段一致，不然表单会无效，又排查半天！！！！！！==



## 八、form表单设计

[参考|Modelform介绍](https://www.cnblogs.com/Creat0r/p/16190289.html)

### 1.何时使用Modelform

表单类继承了`forms.ModelForm`，这个父类**适合于需要直接与数据库交互的功能**，比如新建、更新数据库的字段等。如果表单将用于直接添加或编辑Django模型，则可以使用 `ModelForm`来避免重复书写字段描述。而`forms.Form`则需要手动配置每个字段，**它适用于不与数据库进行直接交互的功能**。

### 2.app表单设计

#### A.login/forms.py

**用户登录**

用户登录不需要对数据库进行任何改动，因此直接继承`forms.Form`就可以了。

```python
class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': 'required'}))
    password = forms.CharField(label="Password", max_length=512,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label='Code', )  # 验证码图片和输入框是一个整体，无法设置样式！！！
	
    # def clean_[字段]这种写法Django会自动调用，来对单个字段的数据进行验证清洗。
    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = models.User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError('This username does not exist Please register first')
        return username
```

**用户注册**

> 注册的字段使用django自带的用户字段，注册完之后跳到登录页面，登录之后跳到用户档案页面，用户必须填写档案，例如头像，别名，号码，邮箱（并邮件确认）之后，才可以进入主界面。

对数据库进行操作的表单应该继承`forms.ModelForm`，可以自动生成模型中已有的字段。

```python
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
            raise forms.ValidationError("密码输入不一致,请重试。")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("your username must be at least 3 characters log")
        elif len(username) > 20:
            raise forms.ValidationError("your username is too long")
        else:
            filter_result = models.User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('your username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        filter_result = models.User.objects.filter(email__exact=email)
        if len(filter_result) > 0:
            raise forms.ValidationError("your email already exists")
        return email
```

这里我们覆写了`password`字段，因为通常在注册时需要重复输入`password`来确保用户没有将密码输入错误，所以覆写掉它以便我们自己进行数据的验证工作。`def clean_password2()`中的内容便是在验证密码是否一致了。==`def clean_[字段]`这种写法Django会自动调用，来对单个字段的数据进行验证清洗。==

覆写某字段之后，内部类`class Meta`中的定义对这个字段就没有效果了，所以`fields`不用包含`password`。[参考](https://www.dusaiphoto.com/article/32/)



## 九、部署到阿里云

[参考|刘江的博客教程](https://www.liujiangblog.com/course/django/181)

[Liunx之Ubuntu下Django+uWSGI+nginx部署](http://www.chenxm.cc/article/87.html)

[使用 Nginx 和 Gunicorn 部署 Django 博客](https://zmrenwu.com/courses/django-blog-tutorial/materials/15/)
