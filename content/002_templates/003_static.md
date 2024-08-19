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
    color: #333333; /* Aplica a cor da fonte para todos esses elementos */
}
```
