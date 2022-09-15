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

### Criar uma verção:

```
  alembic revision -m "Descrição"
```
* Vai ser criado um arquivo onde podemos usar o SQLAlchemy para montagem do banco de dados
> a1ad349f9bf9_Descrição.py

```python

  """create user table

Revision ID: a1ad349f9bf9
Revises: 
Create Date: 2022-09-15 10:32:33.368806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1ad349f9bf9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

```

## Para executar essa verção e criar a tabela:

```python
  alembic upgrade head
```

## Para criar uma geração de migrações automática sem precisar do ORM da versão se cria:
> Exemplo: models.py

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(Strig(50), nullable=False)
```

### Depois no arquivo env.py coloca:
```python

  from < caminho >.models import Base
  
  ...
  
  target_metadata = Base.metadata
```

### comando de geração de versão

```
  alembic revision --autogenerate -m "Descrição"
```


