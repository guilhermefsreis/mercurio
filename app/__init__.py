from vibora import Vibora
from vibora.router import RouterStrategy
from .api import api
from .user.views import user_api
from app.user.model import db

app = Vibora(router_strategy=RouterStrategy.CLONE)

app.add_blueprint(user_api, prefixes={'v1': '/v1'})
app.add_blueprint(api, prefixes={'v1': '/v1'})

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
