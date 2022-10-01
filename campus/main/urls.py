from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'main'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^index', views.IndexView.as_view(), name='indexview'),
    re_path('^categories', views.CategoryView.as_view(), name='categoryview'),
    path('^articles/<int:id>/', views.ArticleView.as_view(), name='articleview'),
    re_path('^files', views.files),
    re_path('^links', views.links),
    re_path('^search', views.search),
    re_path('^logout', views.logout, name='logout'),
]
