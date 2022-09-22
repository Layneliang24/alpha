from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'home'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    path('profile/', views.profile),
    path('edit/', views.edit),
    path('articles/', views.articles),
    path('files/', views.files),
    path('links/', views.links),
    path('reset/', views.reset),
]
