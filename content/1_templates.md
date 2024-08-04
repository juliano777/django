## Templates

Bla bla bla

Criar um diretório de *templates* dentro do diretório da app `recipes`:
```bash
mkdir recipes/templates
```
  
Criação de *templates*:
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
</body>
</html>
```

Alterar o arquivo de *views* da app `recipes`:
```bash
vim recipes/views.py
```
```python
#from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
```    

Verificar o conteúdo do arquivo de `apps.py` em `recipes`:
```bash
cat recipes/apps.py 
```
```
from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
```
Nota-se que o nome da *app* é `recipes`.    
   

Editar o arquivo de configurações do projeto e adicionar `recipes`:
```bash
vim projeto_curso_django/settings.py
```
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 
    'recipes',
)
```
Teste novamente os endereços:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about)
- [http://127.0.0.1:8000/contact](http://127.0.0.1:8000/contact)

Agora, em vez de uma simples mensagem um arquivo HTML foi renderizado conforme
a requisição.
