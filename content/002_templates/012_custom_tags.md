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

from django.template import Library as template_Lib

register = template_Lib()


@register.simple_tag
def randpass(plength: int, digits: bool, special: bool) -> str:

    # Characters
    c = s_ascii_letters

    if digits:
        c += s_digits

    if special:
        c += s_punctuation

    pw = ''

    for _ in range(int(plength)):
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
Redefinir a função `home`:
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

Crie a função `type_cast` em `core/utils.py`:
```bash
vim core/utils.py
```
```python
def type_cast(value: str, type_, default: str):
    '''
    Convert any value to any type.
    If this is not possible a default value will assume.
    '''
    try:
        if value is not None:
            return type_(value)
        else:
            return type_(default)

    except (ValueError, TypeError):
        return type_(default)
```

Altere o arquivo de *views* da *app* recipes:
```bash
vim recipes/views.py
```

Adicione uma nova importação (adicione no final deles):
```python
from core.utils import type_cast
```

Modifique a *view* `home`:
```python
def home(request):
    plength = type_cast(request.GET.get('plength'), int, 7)
    digits = type_cast(request.GET.get('digits'), bool, True)
    special = type_cast(request.GET.get('special'), bool, True)
    cntxt = {'plength': plength, 'digits': digits, 'special': special}
    return render(request, 'home.html', context=cntxt)
```

Senha de 30 caracteres, sem dígitos e sem caracteres especiais:  
http://localhost:8000/?plength=30&digits=&special=  
  
Senha de 30 caracteres e sem caracteres especiais:  
http://localhost:8000/?plength=30&special=

Senha de 30 caracteres e sem dígitos:
http://localhost:8000/?plength=30&digits=

Observe que para ter um valor `False` é necessário que após o sinal de igual
(`=`) não tenha qualquer valor.
