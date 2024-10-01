# Filtros customizados

Assim como em *tags* customizadas é necessário criar o diretório
`templatetags` e claro, o arquivo `__init__.py` dentro dele, porém isso foi
previamente feito.  
   
Criar o arquivo `custom_filters.py`:
```bash
vim recipes/templatetags/custom_filters.py
```
```python
from django.template import Library as template_Lib

register = template_Lib()

# Cube a number
@register.filter(name='cube')
def cube(value: int) -> int:
    try:
        return value ** 3
    except TypeError as e:
        print(f'Error!:\n{e}')

# First letter
@register.filter(name='first_letter')
def first_letter(value: str) -> str:
    return value[0]

# Slicing
@register.filter(name='slicer')
def slicer(value: str, intrvl: str) -> str:    
    intrvl = intrvl.split(',')
    start = intrvl[0]
    end = intrvl[1]
    return value[int(start):int(end)]
```
Devido ao fato de não poder passar mais que um parâmetro, a última função
recebe uma *string* no formato "N,N", indicando número de início e fim do
fatiamento. E por fim esse valor de texto é transformado em uma lista
extraindo os dois números.


Editar o *template* `home.html`:
```bash
vim recipes/templates/home.html
```
```html
{% extends 'base.html' %}
{% load custom_tags %}
{% load custom_filters %}

{% block title %}Home page{% endblock %}

{% block content %}
    <br />
    &nbsp;<b>Sugestão de senha aleatória</b>:
    &nbsp;{% randpass plength digits special %}<br />    
    &nbsp;A quantidade de caracteres da senha é {{ plength }} e seu cubo é: 
        {{ plength|cube }}<br />
    &nbsp;Palavra: "Foo"; primeira letra: {{ 'Foo' | first_letter }}<br />
    &nbsp;"PostgreSQL"; da oitava à décima letra: 
        {{ 'PostgreSQL' | slicer:'7,10' }}
    
{% endblock %}
```

Foi mantido o exemplo anterior de *tag* personalizada e agora em adição tem-se
filtros personalizados também.
