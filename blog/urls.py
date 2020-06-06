from django.conf.urls import url
from django.urls import re_path

from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^post/(?P<slugInput>[\w-]+)', views.lihatPost, name='tampilPost'),
    re_path(r'^category/(?P<kategoriInput>[\w-]+)', views.lihatKategori, name='tampilByKategori'),
    re_path(r'^create/', views.create, name='create')
]
