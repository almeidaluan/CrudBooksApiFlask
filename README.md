## Como rodar o projeto

```sh
    export FLASK_APP=app
    export FLASK_ENV=Development
    export FLASK_DEBUG=True
```

```
    flask db init - Cria a pasta de migrations.

    flask db migrate - Cria a migration do model.

    flask db upgrade - Persiste a migration no banco.
```

#### Tecnologias Utilizadas

    - flask - Framework web
    - flask-sqlalchemy - ORM
    - flask-migrate - Criação das migrations
