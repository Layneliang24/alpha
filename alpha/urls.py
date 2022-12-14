from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('captcha/', include('captcha.urls')),  # 图形验证码功能。要在主项目下添加。
                  path('mdeditor/', include('mdeditor.urls')),  # 为实现markdown功能，不清楚有啥异常
                  re_path(r'^$', include(('login.urls', 'login'), namespace='empty')),      # 命名一定不能重复
                  re_path(r'^login/', include(('login.urls', 'login'), namespace='login')),  # 将路由分发给下面的app处理
                  re_path(r'^home/', include(('home.urls', 'home'), namespace='home')),
                  re_path(r'^post/', include(('post.urls', 'post'), namespace='post')),
                  re_path(r'^main/', include(('main.urls', 'main'), namespace='main')),
                  re_path(r'^introduction/', include(('introduction.urls', 'introduction'), namespace='introduction')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 加上这句至关重要，不然照片不显示

if settings.DEBUG:  # 添加媒体文件url,生产环境下使用
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
