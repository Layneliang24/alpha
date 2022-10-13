from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'post'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^post', views.post),
    re_path('^article', views.PostArticleView.as_view(), name='article'),
    re_path('^file', views.PostFileView.as_view(), name='file'),
    re_path('^link', views.PostLinkView.as_view(), name='link'),
]
