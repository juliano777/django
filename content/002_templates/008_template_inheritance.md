# Herança de template

Segundo a própria documentação, é a parte mais complexa e poderosa do motor de
*templates* do Django.  
Seu conceito basei-se em permitir reutilização de partes comuns de *templates*
entre diferentes páginas.  
Através de um modelo (um *template* "esqueleto"), cujo conteúdo são os
elementos comuns e determina blocos que os *templates* que o herdaram podem
sobrescrever.  
Através da *tag* `{% extends %}` defini-se que um template é herdado de outro.  
Há também a *tag* `{% block %}` que tem como função ser um espaço reservado
para um conteúdo e ser o conteúdo que substituirá o espaço reservado. Nos
*templates* base (que serão herdados), a *tag* `block` é o espaço reservado
que será substituído por um bloco no *template* "filho" (que herda), cujo nome
de bloco será o mesmo. Em *templates* filhos a *tag* `block` é o conteúdo que
substituirá o espaço reservado no *template* herdado com o mesmo nome.  
  
Sintaxe:

```
{% block nome_do_bloco %}
<conteúdo>
{% endblock %}
```

ou

```
{% block nome_do_bloco %}
<conteúdo>
{% endblock nome_do_bloco %}
```
<br />   


Criação do *template* base:
```bash
vim recipes/templates/base.html
```
```html
{% load static %}

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        <!-- Título da página a ser substituído -->
        {% block title %}Novo título{% endblock %}
    </title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    {% block content %}
    <p>Conteúdo a ser substituído</p>
    {% endblock %}
</body>
</html>
```


Modificar o arquivo `home.html` de forma que ele herde `base.html`:
```bash
vim recipes/templates/home.html
```
```html
{% extends 'base.html' %}

{% block title %}Home page{% endblock %}

{% block content %}
    <h1>Página inicial</h1>
    <p>Este é o conteúdo específico desta página.</p>
{% endblock %}
```

Modificar o arquivo `about.html` de forma que ele herde `base.html`:
```bash
vim recipes/templates/about.html
```
```html
{% extends 'base.html' %}

{% block title %}About{% endblock %}

{% block content %}
    <h1>Sobre</h1>
    Bla bla bla
{% endblock %}
```

Editar o arquivo de *views* da app `recipe`:
```bash
vim recipes/views.py
```
Alterar somente as funções `home` e `about`:
```python
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
```
Com o uso de herança de *templates*, nesse caso não havia mais a necessidade
de usar contextos nas funções.  
   
Testando no navegador os endereços:  

`http://localhost:8000`  
`http://localhost:8000/about`




