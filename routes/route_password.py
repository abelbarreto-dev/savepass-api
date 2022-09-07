import json
from fastapi import APIRouter
from models.password import Password
from routes.routes import all_routes
from resource.password_resource import PasswordResource


route_password = APIRouter()
pass_routes = all_routes['password']
pass_resource = PasswordResource()


@route_password.post(pass_routes['new'])
async def post_password(password: Password) -> json:
    return pass_resource.create_password(password=password)


@route_password.get(pass_routes['get_id'])
async def get_by_id_password(id: int = 0) -> json:
    return pass_resource.get_password_by_id(id=id)


@route_password.get(pass_routes['get_all'])
async def get_all_passwords(id: int = 0) -> json:
    return pass_resource.get_passwords_all(id=id)


@route_password.get(pass_routes['search'])
async def get_search_password(**kwargs) -> json:
    return pass_resource.get_password_search(**kwargs)


@route_password.put(pass_routes['update'])
async def put_password(password: Password) -> json:
    return pass_resource.update_password(password=password)


@route_password.delete(pass_routes['delete'])
async def del_password(id: int = 0) -> json:
    return pass_resource.delete_password(id=id)
