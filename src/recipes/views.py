from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    cntxt = {'name': 'Página inicial'}
    return render(request, 'home.html', context=cntxt)

def contact(request):
    cntxt = {'name': '+5511999999999999'}
    return render(request, 'contact.html', context=cntxt)

def about(request):
    cntxt = {'name': 'Bla bla bla'}
    return render(request, 'about.html', context=cntxt)

