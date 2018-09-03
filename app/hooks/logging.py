from vibora import Request
from vibora.blueprints import Blueprint
from vibora.hooks import Events

teste = Blueprint()


@teste.handle(Events.BEFORE_ENDPOINT)
async def before_request(request: Request):
    print("passei aqui")