from pony.orm import db_session
from .model import User


@db_session
def save(model):
    User(name=model['name'])
