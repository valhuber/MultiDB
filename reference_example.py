
""" reference example
BaseA = declarative_base()

BaseB = declarative_base()

class User(BaseA):
    # ...

class Address(BaseA):
    # ...


class GameInfo(BaseB):
    # ...

class GameStats(BaseB):
    # ...


Session = sessionmaker()

# all User/Address operations will be on engine 1, all
# Game operations will be on engine 2
Session.configure(binds={BaseA:engine1, BaseB:engine2})

# https://gist.github.com/lmyyao/37157fff3ba90889d7c1e0f9dc774253

"""

from venv import create
import config
from sqlalchemy import (String,
                        Integer,
                        engine_from_config,
                        create_engine,
                        Column)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as SQLAlchemy

import database.models_todo  # opens multi_db
import database.models  # opens db

engines = {
    'drivers':create_engine(config.Config.SQLALCHEMY_DATABASE_URI),
    'dispatch':create_engine(config.Config.SQLALCHEMY_DATABASE_URI_TODO)
}
debug_models = database.models.Base  # class 'sqlalchemy.orm.decl_api.DeclarativeMeta
debug_models_todo = database.models_todo.BaseToDo

engine_1 = create_engine(config.Config.SQLALCHEMY_DATABASE_URI)
engine_2 = create_engine(config.Config.SQLALCHEMY_DATABASE_URI_TODO)
Session = sessionmaker()

Session.configure(binds={
    database.models.Base:          engine_1,
    database.models_todo.BaseToDo: engine_2 })

session = Session()

verify_todo = session.query(database.models_todo.Todo).first()
print(f'\n\n*** Success\n\n\ttodo access - verify_todo: {str(verify_todo)}')
verify_customer = session.query(database.models.Customer).first()
print(f'\n\tverify_cust: {str(verify_customer)}\n')

pass