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
cat << EOF > src/my_project/db.conf
DB_HOST = 'localhost'
DB_NAME = 'db_django'
DB_USER = 'user_django'
DB_PASSWORD = '123'
DB_PORT = 5432
DB_OPTIONS = '-c search_path=ns_django,public'
EOF
```

Modifique a sessão “Database” conforme abaixo:
```python
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Database configuration file location
DB_CONF_FILE = f'{BASE_DIR}/my_project/db.conf'

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