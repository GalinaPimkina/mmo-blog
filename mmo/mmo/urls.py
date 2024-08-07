"""
URL configuration for mmo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.decorators import login_required
from ckeditor_uploader.views import upload
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ads.urls', namespace='ads')),
    path('users/', include('users.urls', namespace='users')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


admin.site.site_header = "Панель администратора"
admin.site.index_title = ""