
Preparativos via bash
```bash
# Criação do ambiente virtual
python3 -m venv /tmp/venv

# Habilitar o novo ambiente virtual
source /tmp/venv/bin/activate

# Criação do arquivo de pacotes necesários
cat << EOF > /tmp/requirements.txt
django
psycopg
configobj
ipython
EOF

# Atualizar o pip
pip install -U pip

# Instalar os pacotes
pip install -r /tmp/requirements.txt
```


```bash
# Criação de um projeto Django
django-admin startproject projeto_curso_django

# Renomear a pasta criada para src, assim evitando confundir com a subpasta de
# mesmo nome
mv projeto_curso_django src
```