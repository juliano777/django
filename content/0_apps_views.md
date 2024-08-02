## Django apps e views

Criar um novo app de receitas:
```bash
./manage.py startapp recipes
```

Visualizar o conteúdo do diretório do app:
```bash
tree recipes/
```
```
recipes/
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

2 directories, 7 files
```

Criar views para o app:
```bash
# Editar o arquivo de views do app
vim recipes/views.py
```
```python
from django.http import HttpResponse
#from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    return HttpResponse('Home')

def contact(request):
    return HttpResponse('contato')

def about(request):
    return HttpResponse('sobre')        
```

Criar URLs para o app:
```bash
# Editar o arquivo de URLs do app
vim recipes/urls.py
```
```python
from django.urls import path

#
from recipes.views import about
from recipes.views import contact
from recipes.views import home

urlpatterns = (
    path('', home),
    path('about', about),
    path('contact', contact),
)
```


Criar URL:
```bash
# Editar o arquivo de URLs
vim projeto_curso_django/urls.py
```

```python
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # Dentro de /
)
```
