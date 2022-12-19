# Multi DB Projects

## Goals

[This POC](https://github.com/valhuber/MultiDB) (runs in codespaces, explore with ".") is intended to:

* Demonstrate how to handle multiple databases in an API Logic Server Project.

    * This is a copy of the sample project, with an additional _Todo_ database

&nbsp;

Automated support is not yet available, but envisioned, perhaps as follows:

```bash
ApiLogicServer add-database --db_url=XX --bind_name=yy
```

&nbsp;

## Issues

## Table Name Collisions

SAFRS creates endpoint based on table names.  Since 2 databases might have the same table name, these might collide.

> Should SARFS provided an option to create endpoint name from __class name__?

> This might also be regarded as _more friendly_ - API is not  restricted to table names.

&nbsp;

## Setup and Test

Should run using the default Launch Configuration.  Verify by running the admin app, or cURL commands:

```
curl -X 'GET' \
  'http://localhost:5656/api/Category/1/?fields%5BCategory%5D=Id%2CCategoryName%2CDescription' \
  -H 'accept: application/vnd.api+json' \
  -H 'Content-Type: application/vnd.api+json'
```
and,

```bash
curl -X 'GET' \
  'http://localhost:5656/api/todos/?fields%5BTodo%5D=task%2Ccategory%2Cdate_added%2Cdate_completed%2Cstatus%2Cposition&page%5Boffset%5D=0&page%5Blimit%5D=10&sort=id' \
  -H 'accept: application/vnd.api+json' \
  -H 'Content-Type: application/vnd.api+json'
```

&nbsp;

### Background: SQLAlchemy ```Binds```

SQLAlchemy supports the concept of Binds, to support multiple database access within a session, e.g.:

```python
    flask_app.config.update(SQLALCHEMY_BINDS = \
        {'todos-bind': flask_app.config['SQLALCHEMY_DATABASE_URI_TODO']})
```

Note the Bind name: `todos-bind`

&nbsp;

## Setup Steps

Follow the steps below to add multiple database support to your existing API Logic Project.  

* Use this project as a reference example

* Search for ```# Multi-DB```

&nbsp;

### 1. Add models file `models_todo.py`

Add your models_<bind> to the `database` directory:

1. Create this using API Logic Server in a _separate_ project
2. Alter it as illustrated in `models_todo.py`:
    1. Declare _additional base classes_
    2. _Use additional base classes_ on each class definition
    3. _Identify the bind_

&nbsp;

### 2. _Define URI_ in `config.py`

This identifies the physical location of the database.

&nbsp;

### 3. Update `api_logic_server_run.py` - open models, update binds, expose API

Note the following code:

```python
            multi_db_enabled = True    # Multi-DB: open models, update binds, expose API
            if multi_db_enabled:
                from api import expose_api_models_todo
                from database import models_todo
                flask_app.config.update(SQLALCHEMY_BINDS = \
                    {'todos-bind': flask_app.config['SQLALCHEMY_DATABASE_URI_TODO']})
                app_logger.info(f"\nTODOs Config complete - database/models_todo.py"
                    + f'\n -- with bind: {session.bind}'
                    + f'\n -- {len(database.models_todo.BaseToDo.metadata.tables)} tables loaded')
                expose_api_models_todo.expose_models_on_existing_api(safrs_api)
```

&nbsp;

### 4. Update your `ui/admin/admin.yaml`


&nbsp;

