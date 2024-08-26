# Templates globais e arquivos estáticos globais

Criar estrutura de diretórios dentro de `src`:
```bash
mkdir -p global/{templates,static/css}
``` 

Verificar a estrutura:
```bash
tree global/
```
```
global/
├── static
│   └── css
└── templates
```

Mover arquivos que na verdade são de interesse comum:
```bash
# Movendo templates
mv recipes/templates/head.html global/templates/

# Movendo arquivos estáticos
mv recipes/static/css/styles.css global/static/css/
```

Adicione as seguintes linhas ao final do arquivo considerando as linhas em
branco também:
```bash
vim projeto_curso_django/settings.py
```
```python

# Static files directories
STATICFILES_DIRS = (f'{BASE_DIR}/global/static', )

```

Mude também a variável `TEMPLATES`:
```python
TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (f'{BASE_DIR}/global/templates', ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
        },
    },
)
```
Note que `f'{BASE_DIR}/global/templates'` foi adicionado como diretório de
*templates*.  
A variável `BASE_DIR` é a pasta raiz do projeto.  
  
  
