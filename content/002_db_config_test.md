# Configuração e teste de conexão com o banco de dados

## Schema 

Também conhecido com namespace, o schema é um tipo de objeto de banco de dados
cujo propósito é ser uma camada de organização hierárquica que está logo
abaixo de uma base de dados.  
No PostgreSQL, “`public`” é o schema padrão, mas você pode criar seus próprios
namespaces para organizar outros tipos de objetos como tabelas, views,
functions, procedures etc.  
  
*Hierarquia de objetos de bancos de dados*  
```
- Server
   └─ PostgreSQL Instance (Port 5432 by default)
       ├─ Role (Users and Groups)
       ├─ Tablespace
       └─ Database
           ├─ Trigger
           ├─ Extension
           ├─ Language
           └─ Schema      
               ├─ Table
               ├─ View
               ├─ Materialized View
               ├─ Sequence
               ├─ Function
               └─ Procedure
```

```bash
# Heredoc para criação do arquivo de configuração de base de dados
cat << EOF > src/projeto_curso_django/db.conf
DB_HOST = 'localhost'
DB_NAME = 'db_django'
DB_USER = 'user_django'
DB_PASSWORD = '123'
DB_PORT = 5432
DB_OPTIONS = '-c search_path=ns_django,public'
EOF
```

Modifique a sessão “Database” conforme abaixo:
```bash
# Editar o settings.py
vim src/projeto_curso_django/settings.py
```
```python
# Database

# Database configuration file location
DB_CONF_FILE = f'{BASE_DIR}/projeto_curso_django/db.conf'

# Read the configurations from file
DB_CONFIG = ConfigObj(DB_CONF_FILE)

# Database connection parameters

DB_HOST = DB_CONFIG['DB_HOST']
DB_NAME = DB_CONFIG['DB_NAME']
DB_USER = DB_CONFIG['DB_USER']
DB_PASSWORD = DB_CONFIG['DB_PASSWORD']
DB_PORT = DB_CONFIG['DB_PORT']
DB_OPTIONS = DB_CONFIG['DB_OPTIONS']

DATABASES = {
             'default': {
                         'ENGINE': 'django.db.backends.postgresql',
                         'NAME': DB_NAME,
                         'USER': DB_USER,
                         'PASSWORD': DB_PASSWORD,
                         'HOST': DB_HOST,
                         'PORT': DB_PORT,
                         'OPTIONS': {'options': DB_OPTIONS},
                         }
            }
```
   
Verificar a árvore de diretórios de arquivos:
```bash
tree src/
```
```
src/
├── manage.py
└── projeto_curso_django
    ├── asgi.py
    ├── db.conf
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   └── settings.cpython-310.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py

2 directories, 9 files
```

   
Logo após os imports adicione a seguinte linha:
```python
from configobj import ConfigObj
```

Entrar no shell do banco de dados
```bash
./src/manage.py dbshell
```

```sql
-- Criar um esquema (namespace) para o Django
CREATE SCHEMA ns_django;
```

Verificar a criação do schema consultando todos schemas que não são catálogos
(metadados do PostgreSQL):
```sql
SELECT
    nspname AS namespace
FROM pg_catalog.pg_namespace
WHERE nspname !~ '(^pg_|information_schema)';
```
```
 namespace 
-----------
 public
 ns_django
```

Banco de dados configurado, então agora pode-se rodar a "migração" inicial, 
que significa levar os dados iniciais do Django para o sistema gerenciador de
banco de dados (SGBD), que neste caso é o PostgreSQL.
```bash
./manage.py migrate
```
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
```
   
Após a migração feita, com o comando abaixo entrar no prompt do banco de dados:
```bash
./manage.py dbshell
```
```
Expanded display is used automatically.
psql (16.1 (Ubuntu 16.1-1.pgdg22.04+1), server 16.0 (Debian 16.0-1.pgdg120+1))
Type "help" for help.

db_django=> 
```
Por ser PostgreSQL o prompt padrão é o psql, que é o cliente em modo texto
padrão do SGBD.  
  

Verificar todas as tabelas do schema ns_django:
```
\dt ns_django.*
```
```
                      List of relations
  Schema   |            Name            | Type  |    Owner    
-----------+----------------------------+-------+-------------
 ns_django | auth_group                 | table | user_django
 ns_django | auth_group_permissions     | table | user_django
 ns_django | auth_permission            | table | user_django
 ns_django | auth_user                  | table | user_django
 ns_django | auth_user_groups           | table | user_django
 ns_django | auth_user_user_permissions | table | user_django
 ns_django | django_admin_log           | table | user_django
 ns_django | django_content_type        | table | user_django
 ns_django | django_migrations          | table | user_django
 ns_django | django_session             | table | user_django
(10 rows)
```
Essas tabelas foram criadas ao fazer a migração inicial.  
São tabelas que contêm metadados do Django.  
  
