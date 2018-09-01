from vibora.responses import JsonResponse
from vibora.blueprints import Blueprint

api = Blueprint()


@api.route('/')
async def home():
    return JsonResponse({'hello': 'world'})
