import json
import re
from vibora.responses import JsonResponse
from vibora.blueprints import Blueprint
from vibora import Request
from .dao import save, retrieve, delete

user_api = Blueprint()


@user_api.route('/user')
async def get():
    users = retrieve()
    return JsonResponse(users, status_code=200)


@user_api.route('/user', methods=['POST'])
async def create(request: Request):
    body = await request.stream.read()
    user = json.loads(body)
    save(user)
    return JsonResponse(user, status_code=201)


@user_api.route('/user/<user_id>', methods=['DELETE'])
async def remove(user_id: int):
    delete(user_id)
    return JsonResponse({}, status_code=204)
