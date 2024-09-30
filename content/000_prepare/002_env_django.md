## Preparativos do ambiente Django

Preparativos via bash

Criação do ambiente virtual:
```bash
python3 -m venv /tmp/venv
```

Habilitar o novo ambiente virtual:
```bash
source /tmp/venv/bin/activate
```

Criação do arquivo de pacotes necesários:
```bash
cat << EOF > /tmp/requirements.txt
django
psycopg
configobj
ipython
EOF
```

Atualizar o pip:
```bash
pip install -U pip
```

Instalar os pacotes:
```bash
pip install -r /tmp/requirements.txt
```

Criação de um projeto Django:
```bash
# Criação do diretório que conterá os códigos
mkdir src

# Criação do projeto dentro do diretório
django-admin startproject projeto_curso_django src/
```

Entrar no diretório src:
```bash
cd src
```

> **_Nota:_**  A partir de agora todos os comandos serão dados a partir do
> diretório **`src`**.

Criar o diretório `core`, o qual conterá códigos Python úteis para todo o
projeto:
```bash
mkdir core
```

Criar os arquivos `utils.py` e `utils.py` dentro de `core`, sendo que o último
é para que o diretório possa ser tratado como pacote:

```bash
touch core/{utils,__init__}.py
```

Verificar o conteúdo do diretório atual:
```bash
tree
```
```
.
├── manage.py
└── projeto_curso_django
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

2 directories, 6 files
```

Testando o servidor local:
```bash
./manage.py runserver
```
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 02, 2024 - 14:49:43
Django version 5.0.7, using settings 'projeto_curso_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Sobre esta mensagem:  
```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
```

Isso se refere à base de dados do Django em si.  
Após a configuração do banco de dados isso será resolvido.

Por hora vamos cancelar utilizando a combinação de teclas `Ctrl + C`.
