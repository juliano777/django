# Tags customizadas

https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/

Crie o diretório `templatetags` dentro do diretório da *app* `recipes` e
também criar so arquivo `__init__.py` para garantir que o diretório seja
tratado como um pacote Python e o arquivo `custom_tags.py`:
```bash
mkdir recipes/templatetags
touch recipes/templatetags/{__init__.py,custom_tags.py}
```

Edite o arquivo de *tags* customizadas:
```bash
vim recipes/templatetags/custom_tags.py
```
```python
from random import choice as r_choice
from string import ascii_letters as s_ascii_letters
from string import digits as s_digits
from string import punctuation as s_punctuation

from django.template import Library as template_lib

register = template_lib()


@register.simple_tag
def randpass(
    plength: int=10,
    digits: bool=True,
    special: bool=True,
) -> str:

    # Characters
    c = s_ascii_letters

    if digits:
        c += s_digits

    if special:
        c += s_punctuation

    pw = ''

    for _ in range(plength):
        pw += r_choice(c)

    return pw
```

Edite o *template* `home.html`:
```bash
vim recipes/templates/home.html
```
```html
{% extends 'base.html' %}
{% load custom_tags %}

{% block title %}Home page{% endblock %}

{% block content %}
    Lista de teste: {% ul 'Foo' 5 %}
    
{% endblock %}
```

Alterar o arquivo de *views* da *app* `recipes`:
```bash
vim recipes/views.py
```
Redefinir a funçãso `home`:
```python

def home(request, plength, digits, special):
    # Tenta converter o valor para um número inteiro
    try:
        numero = int(request.GET.get('numero'))
    except:
        # Caso algo ter errado seu valor será nulo
        numero = None
    return render(request, 'home.html', context={'numero': numero})
```

http://localhost:8000/?plength=7&digits=0&special=0
http://localhost:8000/?plength=15&digits=0