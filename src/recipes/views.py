from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    # Tenta converter o valor para um número inteiro
    try:
        numero = int(request.GET.get('numero'))
    except:
        # Caso algo ter errado seu valor será nulo
        numero = None
    return render(request, 'home.html', context={'numero': numero})

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

