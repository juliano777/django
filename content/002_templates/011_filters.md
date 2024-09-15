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


https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#filters

https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-filters