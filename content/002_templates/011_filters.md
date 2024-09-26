# Filtros

Filtros de *templates* Django é um interessante recurso que permite formatar 
e / ou manipular dados antes da exibição dos mesmos.  
Os filtros são aplicados diretamente nas variáveis de contexto e fornecem um
jeito simples de alterar valores de forma simplicada em vez de adicionar uma
lógica complexa.
  
Sintaxe:
```  
{{ variavel|filtro }}
```

Pode-se também usar encadeamento de filtros:

```
{{ variavel|filtro1|filtro2|...|filtroN }}
```

Referências:

[https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#filters)

[https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-filters)

Edite o arquivo de *views* da *app* `recipes` e modifique `home`:
```bash
vim recipes/views.py 
```
```python
def home(request):
    books = (
        {
            'title': 'O Hobbit',
            'author': {'name': 'J. R. R. Tolkien', 'b_year': 1892}
        },
        {
            'title': 'The Call of Cthulhu',
            'author': {'name': 'H. P. Lovecraft', 'b_year': 1890}
        },
        {
            'title': 'Conan O Bárbaro',
            'author': {'name': 'Robert E. Howard', 'b_year': 1906}
        },
        {
            'title': 'Histórias Extraordinárias',
            'author': {'name': 'Edgar Allan Poe', 'b_year': 1809}
        },
        {
            'title': 'Carrie',
            'author': {'name': 'Stephen King', 'b_year': 1947}
        },
    )

    cities = (
        {'name': 'São Paulo', 'region': 'Sudeste'},
        {'name': 'Macapá', 'region': 'Norte'},
        {'name': 'Natal', 'region': 'Nordeste'},
        {'name': 'Curitiba', 'region': 'Sul'},
        {'name': 'Campo Grande', 'region': 'Centro Oeste'},
    )


    cntxt = {
        'a_text': 'foo',
        'phrase': 'uma frase qualquer',
        'a_number': 7,
        'now': datetime.now(),
        'bool_false': False,
        'bool_true': True,
        'none_var': None,
        'cities': cities,
        'books': books,
        }
    return render(request, 'home.html', context={**cntxt, 'cntxt': cntxt})
```

Note que a variável `context` possui um dicionário interno (`cntxt`) que foi
"explodido";

Edite o *template* `home`:
```bash
vim recipes/templates/home.html
```
```html
{% extends 'base.html' %}

{% block title %}Home page{% endblock %}

{% block content %}
    <h1>Página inicial</h1>
    <h2>Variáveis</h2>    
    
    <!-- Loop na variável cntxt que é um dicionário (chaves e valores)-->
    {% for k, v in cntxt.items %}
        &nbsp;<strong> - {{ k }}</strong> &rarr; {{ v }}<br />        
    {% endfor %}
    
    <!-- Testes com filtros -->
    <h2>Testes com as variáveis do dicionário</h2>
    &nbsp;a_text|upper &nbsp;&rarr;&nbsp;{{ a_text|upper }}<br />
    &nbsp;a_text|add:'2' &nbsp;&rarr;&nbsp;{{ a_text|add:'2' }}<br />
    &nbsp;a_number|add:'2' &nbsp;&rarr;&nbsp;{{ a_number|add:'2' }}<br />
    &nbsp;phrase|title &nbsp;&rarr;&nbsp;
        {{ phrase|title }}<br />
    &nbsp;phrase|capfirst &nbsp;&rarr;&nbsp;
        {{phrase|capfirst }}<br />
    &nbsp;"Copo d'água"|addslashes &nbsp;&rarr;&nbsp;
        {{ "Copo d'água"|addslashes }}<br />
    &nbsp;now|date:'Y-m-d H:i' &nbsp;&rarr;&nbsp;
        {{ now|date:'Y-m-d H:i' }}<br />
    &nbsp;phrase|cut:' ' &nbsp;&rarr;&nbsp;
        {{phrase|cut:' ' }}<br />
    &nbsp;phrase|upper|slice:':11'|default:'Sem valor' &nbsp;&rarr;&nbsp;
        {{phrase|upper|slice:':11'|default:'Sem valor' }}<br />
    &nbsp;bool_false|default:'Bla bla bla' &nbsp;&rarr;&nbsp;
        {{ bool_false|default:'Bla bla bla' }}<br />
    &nbsp;bool_true|default:'Bla bla bla' &nbsp;&rarr;&nbsp;
        {{ bool_true|default:'Bla bla bla' }}<br />
    &nbsp;none_var|default_if_none:'Variável nula' &nbsp;&rarr;&nbsp;
        {{ none_var|default_if_none:'Variável nula' }}<br />
    &nbsp;cities|dictsort:'name' &nbsp;&rarr;&nbsp;
        {{ cities|dictsort:'name' }}<br />

    <h2>Loop for</h2>    
    {% for i in books|dictsortreversed:'author.b_year' %}
        &nbsp;* {{ i.title }} - ({{ i.author.name }}, {{ i.author.b_year}})<br />
    {% endfor %}    
    
{% endblock %}

```


