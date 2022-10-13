from django.urls import path, re_path
from . import views

# 正在部署的应用的名称，Django2.0之后，app的urls.py必须配置app_name，否则会报错。
app_name = 'main'

urlpatterns = [
    re_path('^$', views.empty),  # 正则匹配必须用re_path
    re_path('^index', views.IndexView.as_view(), name='indexview'),
    re_path('^categories', views.CategoryView.as_view(), name='categoryview'),
    re_path('^articles/(?P<id>.*)', views.ArticleView.as_view(), name='articleview'),
    re_path('^files', views.FileListView.as_view(), name='filelistview'),
    re_path('^links', views.LinkListView.as_view(), name='linklistview'),
    re_path('^search$', views.SearchView.as_view(), name='search'),
    re_path('^filelist/search$', views.SearchFileListView.as_view(), name='searchfilelistview'),
    re_path('^linklist/search$', views.SearchLinkListView.as_view(), name='searchlinklistview'),
    re_path('^visit/(?P<id>.*)/article$', views.VisitArticleView.as_view(), name='visitarticleview'),
    re_path('^visit/(?P<id>.*)/file$', views.VisitFileView.as_view(), name='visitfileview'),
    re_path('^visit/(?P<id>.*)/link$', views.VisitLinkView.as_view(), name='visitlinkview'),
    re_path('^visit/(?P<id>.*)/article/search$', views.VisitSearchArticleView.as_view(), name='visitsearcharticleview'),
    re_path('^visit/(?P<id>.*)/file/search$', views.VisitSearchFileView.as_view(), name='visitsearchfileview'),
    re_path('^visit/(?P<id>.*)/link/search$', views.VisitSearchLinkView.as_view(), name='visitsearchlinkview'),
    re_path('^logout', views.logout, name='logout'),
]
