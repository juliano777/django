# Templates locais e arquivos estáticos locais

E se quisermos utilizar um template ou arquivos estáticos locais em vez de
globais?  
Há situações que precisamos utilizar algo que esteja local.

## Templates locais

Criar o diretório necessário:
```bash
mkdir recipes/templates/recipes
```
Esse novo diretório tem que estar dentro de `templates` e ter o mesmo nome da
aplicação.
   
Criar um template de teste:
```bash
vim recipes/templates/teste-local.html
```
```html
{% include 'recipes/head.html' %}

<body>
    <h1>{{ name }}</h1>
</body>
Um simples teste notando a mudança de estilo neste template local.
</html>
```

Criar um arquivo `head.html`local:
```bash
vim recipes/templates/recipes/head.html
```
```html
{% load static %}

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{% static 'recipes/css/styles.css' %}">  
</head>
```
Nota-se que na referência à localização do arquivo estático também será de um
arquivo local.  

## Arquivos estáticos locais

Criar o diretório necessário:
```bash
mkdir -p recipes/static/recipes/css
ar o diretório necessário:
```
Dentro de `recipes` foi criada a hierarquia de diretórios `static/recipes/css`
e assim como visto anteriormente no diretório local de *templates* foi
necessário que a pasta dentro de `static` também tivesse o mesmo nome da
*app*.  
   
Criar um arquivo css local:
```bash
vim recipes/static/recipes/css/styles.css
```
```css
body {
    background-color: #006600; /* Verde escuro */
    color: #FFFF00; /* Amarelo */
    font-family: Arial, sans-serif; /* Fonte padrão, pode ser alterada */
    margin: 0;
    padding: 0;
}

p, h1, h2, h3, h4, h5, h6, a, li, span {
    color: #FFFF00; /* Aplica a cor da fonte para todos esses elementos */
}
```
Editar o arquivo de *views* da aplicação *recipes* e adicionar a seguinte
função no final:
```bash
vim recipes/views.py
```
```python
def teste_local(request):
    name = 'Teste local de arquivos estáticos e templates'
    cntxt = {'title': 'TEMPLATE LOCAL', 'name': name}
    return render(request, 'teste-local.html', context=cntxt)
```

Editar o arquivo de URLs da aplicação *recipes*:
```bash
vim recipes/urls.py
```
```python
from django.urls import path

#
from recipes.views import about
from recipes.views import contact
from recipes.views import home
from recipes.views import teste_local

urlpatterns = (
    path('', home),
    path('about', about),
    path('contact', contact),
    path('teste-local', teste_local),
)
```
Para testar acesse: [http://localhost:8000/teste-local](http://localhost:8000/teste-local)