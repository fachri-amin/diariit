from django.shortcuts import render

def index(request):
    context = {
        'heading':'Diariit | Home',
        'judul':'Diariit',
    }
    return render(request,'utama.html',context)