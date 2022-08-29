import json
from fastapi import APIRouter
from models.password import Password
from routes.routes import all_routes
from resource.password_resource import (
    create_password, get_password_by_id, get_passwords_all,
    get_password_search, update_password, delete_password
)


route_password = APIRouter()
pass_routes = all_routes['password']


@route_password.post(pass_routes['new'])
async def post_password(password: Password) -> json:
    return create_password(password=password)


@route_password.get(pass_routes['get_id'])
async def get_by_id_password(id: int = 0) -> json:
    return get_password_by_id(id=id)


@route_password.get(pass_routes['get_all'])
async def get_all_passwords(id: int = 0) -> json:
    return get_passwords_all(id=id)


@route_password.get(pass_routes['search'])
async def get_search_password(**kwargs) -> json:
    return get_password_search(kwargs)


@route_password.put(pass_routes['update'])
async def put_password(password: Password) -> json:
    return update_password(password=password)


@route_password.delete(pass_routes['delete'])
async def del_password(id: int = 0) -> json:
    return delete_password(id=id)
