from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import form_daftar
from .models import FormDaftar
# Create your views here.

def index(request):
    form_pendaftaran = form_daftar(request.POST or None)

    if request.method == 'POST':
        if form_pendaftaran.is_valid():
            form_pendaftaran.save()
            return HttpResponseRedirect('/admin/')
    context ={
        'heading': 'Formulir Pendaftaran',
        'form_pendaftaran':form_pendaftaran,
    }
    return render(request, 'register/index.html', context)