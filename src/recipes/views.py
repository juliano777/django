from datetime import datetime
from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    books = (
        {
            'title': 'O Hobbit',
            'author': {'name': 'J. R. R. Tolkien', 'b_year': 1892}
        },
        {
            'title': 'The Call of Cthulhu',
            'author': {'name': 'H. P. Lovecraft', 'b_year': 1890}
        },
        {
            'title': 'Conan O Bárbaro',
            'author': {'name': 'Robert E. Howard', 'b_year': 1906}
        },
        {
            'title': 'Histórias Extraordinárias',
            'author': {'name': 'Edgar Allan Poe', 'b_year': 1809}
        },
        {
            'title': 'Carrie',
            'author': {'name': 'Stephen King', 'b_year': 1947}
        },
    )

    cities = (
        {'name': 'São Paulo', 'region': 'Sudeste'},
        {'name': 'Macapá', 'region': 'Norte'},
        {'name': 'Natal', 'region': 'Nordeste'},
        {'name': 'Curitiba', 'region': 'Sul'},
        {'name': 'Campo Grande', 'region': 'Centro Oeste'},
    )


    cntxt = {
        'a_text': 'foo',
        'phrase': 'uma frase qualquer',
        'a_number': 7,
        'now': datetime.now(),
        'bool_false': False,
        'bool_true': True,
        'none_var': None,
        'cities': cities,
        'books': books,
        }
    return render(request, 'home.html', context={**cntxt, 'cntxt': cntxt})

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

