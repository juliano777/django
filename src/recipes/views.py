from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    d = {
        'Continente': 'América do Sul',
        'País': 'Brasil',
        'Estado': 'São Paulo',
        'Área total': '1.521,202 km²',
        'Altitude': '772 m',
        'Fuso horário': 'Hora de Brasília (UTC−3)',
    }

    return render(request, 'home.html', context={'cntxt': d})

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

