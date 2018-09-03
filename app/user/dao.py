from pony.orm import db_session
from .model import User


@db_session
def save(model):
    User(name=model['name'])


@db_session
def retrieve():
    return User.select_by_sql('SELECT * FROM User')


@db_session
def retrieve_by_id(id):
    return User[id]


@db_session
def delete(id):
    User[id].delete()
