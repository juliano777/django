Criar a hierarquia de pastas `static/css` dentro da pasta do app:

```bash
mkdir -p recipes/static/css
```

Criar um exemplo de arquivo css:

```bash
vim recipes/static/css/styles.css
```
```css
body {
    background-color: #f0f0f0; /* Cinza claro */
    color: #333333; /* Cinza escuro */
    font-family: Arial, sans-serif; /* Fonte padrão, pode ser alterada */
    margin: 0;
    padding: 0;
}

p, h1, h2, h3, h4, h5, h6, a, li, span {
    color: #067528; /* Aplica a cor da fonte para todos esses elementos */
}
```

Edite o arquivo `head.html`:
```html
{% load static %}

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
```

Após salvar as alterações atualize a página no navegador para notar as
diferenças de *layout*.