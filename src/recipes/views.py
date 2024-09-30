from datetime import datetime
from django.shortcuts import render
from django.urls import path

from core.utils import type_cast

# Create your views here.

def home(request):
    plength = type_cast(request.GET.get('plength'), int, 7)
    digits = type_cast(request.GET.get('digits'), bool, True)
    special = type_cast(request.GET.get('special'), bool, True)
    cntxt = {'plength': plength, 'digits': digits, 'special': special}
    return render(request, 'home.html', context=cntxt)

def contact(request):
    cntxt = {'title': 'Contact', 'name': '+5511999999999999'}
    return render(request, 'contact.html', context=cntxt)

def about(request):
    return render(request, 'about.html')

def teste_local(request):
    name = 'Teste local de arquivos estáticos e templates'
    cntxt = {'title': 'TEMPLATE LOCAL', 'name': name}
    return render(request, 'teste-local.html', context=cntxt)

def recipe(request, id):
    cntxt = {'title': f'Receita {id}', 'name': f'id: {id}'}
    return render(request, 'recipe.html', context=cntxt)
