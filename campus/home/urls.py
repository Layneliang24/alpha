from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'home'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^center$', views.CenterView.as_view(), name='center'),
    re_path('^center/file$', views.CenterFileView.as_view(), name='file'),
    re_path('^center/link$', views.CenterLinkView.as_view(), name='link'),
    re_path('^center/search/article$', views.SearchArticleView.as_view(), name='search_article'),
    re_path('^center/search/file$', views.SearchFileView.as_view(), name='search_file'),
    re_path('^center/search/link$', views.SearchLinkView.as_view(), name='search_link'),
    re_path('^center/edit/profile/(?P<pk>\d+)$', views.ProfileUpdateView.as_view(), name='profile'),
    re_path('^center/edit/article/(?P<pk>\d+)$', views.ArticleUpdateView.as_view(), name='edit_article'),
    re_path('^center/edit/link/(?P<pk>\d+)$', views.LinkUpdateView.as_view(), name='edit_link'),
    # re_path('^reset', views.reset),
]
