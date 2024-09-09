# URLs dinâmicas

Editar o arquivo de URLs da app `recipes`:
```bash
vim src/recipes/urls.py
```
Nos imports adicione a seguinte linha:
```python
from recipes.views import recipe
```
Adicione-a de forma alfabética para manter o padrão.  
  
Altere tupla `urlpatterns` adicionando mais um elemento:
```python
urlpatterns = (
    path('', home),
    path('about', about),
    path('contact', contact),
    path('teste-local', teste_local),
    path('recipe/<int:id>/', recipe),
)
```
Note que o valor de `id` deve ser um número inteiro.  
   

Editar o arquivo de *views* da app `recipes`:
```bash
vim src/recipes/views.py
```
Apenas adicione a seguinte função ao 
```python
def recipe(request, id):
    cntxt = {'title': f'Receita {id}', 'name': f'{id} - Receita'}
    return render(request, 'recipe.html', context=cntxt)
```

Criar um template novo para teste:
```bash
vim src/recipes/templates/recipe.html
```
```html
{% include 'head.html' %}

<body>
    <h1>{{ name }}</h1>
    Bla bla bla
</body>
</html>
```









