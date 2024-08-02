## Preparativos do ambiente Django

[venv.sh](../scripts/venv.sh)

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
django-admin startproject projeto_curso_django
```

Renomear a pasta criada para src, assim evitando confundir com a subpasta de
mesmo nome:
```bash
mv projeto_curso_django src
```

Entrar no diretório src:
```bash
cd src
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
