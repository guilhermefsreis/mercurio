from pony.orm import *

db = Database()


class User(db.Entity):
    name = Required(str)
