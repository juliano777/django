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


Criação do *template* base:
```bash
# home.html
vim recipes/templates/base.html
```
```html
<body>
    {% block foo %}
    <p>Conteúdo a ser substituído.</p>
    {% endblock %}
</body>
</html>
```

Modificar o arquivo `home.html` de forma que ele herde `base.html`:
```bash
vim recipes/templates/home.html
```
```html
{% include 'head.html' %}

{% extends 'base.html' %}

{% block title %}Página Inicial{% endblock %}

{% block content %}
    <h2>Bem-vindo à página inicial!</h2>
    <p>Este é o conteúdo específico desta página.</p>
{% endblock %}
```
