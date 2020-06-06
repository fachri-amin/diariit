from django.contrib import admin
from django.urls import path, re_path, include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^blog/', include('blog.urls', namespace='blog')),
    re_path(r'^register/', include('register.urls', namespace='register')),
]