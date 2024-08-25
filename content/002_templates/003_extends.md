# Extender um template

Editar o arquivo de views da app `recipes`:

```bash
vim recipes/views.py
```
```python
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
``` 
Nota-se que agora há duas variáveis de contexto.

Criar o arquivo `head.html`:
```bash
vim recipes/templates/head.html
```
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
```
O arquivo `head.html` receberá a variável de contexto "`title`".  

Recriar os templates existentes:
```bash
vim recipes/templates/home.html
```
```html
{% include 'head.html' %}

<body>
    <h1>Receitas</h1>
    {{ name }}
</body>
</html>
```
```bash
vim recipes/templates/about.html
```
```html
{% include 'head.html' %}

<body>
    <h1>Receitas</h1>
    {{ name }}
</body>
</html>
```
```bash
vim recipes/templates/contact.html
```
```html
{% include 'head.html' %}

<body>
    <h1>Informações de contato</h1>
    {{ name }}
</body>
</html>
```
