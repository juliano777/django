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
from django.template import Library as template_lib

register = template_lib()


@register.simple_tag
def ul(value: str, n_items: int) -> str:
    s = '<ul>'
    for i in range(n_items):
        s = f'{s}\n    <li><b>{value.lower()}</b> {i + 1}</li>'

    return f'{s}\n</ul>'
```

Edite o *template* `home.html`:
```bash
vim recipes/templates/home.html
```
```python
from django.template import Library as template_lib

register = template_lib()


@register.simple_tag
def ul(value: str, n_items: int) -> str:
    s = '<ul>'
    for i in range(n_items):
        s = f'{s}\n    <li><b>{value.lower()}</b> {i + 1}</li>'

    return f'{s}\n</ul>'
```