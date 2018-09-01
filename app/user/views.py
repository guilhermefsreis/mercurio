import json
from vibora.responses import JsonResponse
from vibora.blueprints import Blueprint
from vibora import Request
from .dao import save

user_api = Blueprint()


@user_api.route('/user')
async def get():
    return JsonResponse({'id': 1})


@user_api.route('/user', methods=['POST'])
async def create(request: Request):
    body = await request.stream.read()
    user = json.loads(body)
    save(user)
    return JsonResponse(user)
