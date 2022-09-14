# base_migration
migração com alembic e sqlacodegen

### instalação

```
  pip instal alembic
```

## gerando arquivos do alembic no diretório escolhido ou só '.' :

```
 alembic init .
```

### No arquivo alembic.init procure por **'sqlalchemy.url'** :

> Exemplo: sqlalchemy.url = postgresql://scott:tiger@localhost/test

