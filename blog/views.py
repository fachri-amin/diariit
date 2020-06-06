from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Post
from .forms import CreatePost
# Create your views here.

def index(request):
    ambilPost = Post.objects.all()
    categoriesValues = Post.objects.values('category').distinct()
    context={
        'judul':'BLOG',
        'subjudul':'Kumpulan Blog-blog',
        'posts':ambilPost,
        'categories':categoriesValues,
    }
    return render(request,'blog/blog.html',context)

def lihatPost(request, slugInput):
    tampilPost = Post.objects.get(slug=slugInput)
    context= {
        'tampilkan':tampilPost,
    }
    return render(request, 'blog/lihatPost.html', context)

def lihatKategori(request, kategoriInput):
    tampilKategori = Post.objects.filter(category=kategoriInput)
    categoriesValues = Post.objects.values('category').distinct()
    context= {
        'postByCategory':tampilKategori,
        'judul':'BLOG',
        'subjudul':'Kumpulan Blog-blog',
        'categories':categoriesValues,
    }
    return render(request, 'blog/lihatKategori.html', context)

def create(request):
    tambahPost = CreatePost(request.POST or None)
    kesalahan = None

    if request.method == 'POST':

        if tambahPost.is_valid():
            tambahPost.save()
            return HttpResponseRedirect('/blog/')
        else:
            kesalahan = tambahPost.errors

    context = {
        'judul':'Tambah Post',
        'subjudul':'Posting hal bermanfaat',
        'formCreate':tambahPost,
        'error':kesalahan,
    }
    print(type(kesalahan))

    return render(request, 'blog/create.html', context)
