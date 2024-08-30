from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    cntxt = {'title': 'Home page', 'name': 'Página inicial'}
    return render(request, 'home.html', context=cntxt)

def contact(request):
    cntxt = {'title': 'Contact', 'name': '+5511999999999999'}
    return render(request, 'contact.html', context=cntxt)

def about(request):
    cntxt = {'title': 'About', 'name': 'Bla bla bla'}
    return render(request, 'about.html', context=cntxt)

def teste_local(request):
    name = 'Teste local de arquivos estáticos e templates'
    cntxt = {'title': 'TEMPLATE LOCAL', 'name': name}
    return render(request, 'teste-local.html', context=cntxt)
