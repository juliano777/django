# Função render e context

Alterar o arquivo de *views* de `recipes`:
```bash
# Editar o arquivo de views do app
vim recipes/views.py
```
```python
#from django.http import HttpResponse
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
```

Alteração de *templates*:
```bash
# home.html
vim recipes/templates/home.html
```
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Receitas</title>
</head>
<body>
    <h1>Receitas</h1>
    {{ name }}
</body>
</html>
```
```bash
# about.html
vim recipes/templates/about.html
```
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sobre</title>
</head>
<body>
    <h1>Sobre</h1>
    {{ name }}
</body>
</html>
```
```bash
# contact.html
vim recipes/templates/contact.html
```
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informações de contato</title>
</head>
<body>
    <h1>Informações de contato</h1>
    {{ name }}
</body>
</html>
```

Teste novamente os endereços:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about)
- [http://127.0.0.1:8000/contact](http://127.0.0.1:8000/contact)
