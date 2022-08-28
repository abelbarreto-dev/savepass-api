import json
from fastapi import APIRouter
from models.password import Password
from routes.routes import all_routes


route_password = APIRouter()
pass_routes = all_routes['password']


@route_password.post(pass_routes['new'])
async def create_password(password: Password) -> json:
    pass


@route_password.get(pass_routes['get_id'])
async def get_password_by_id(id: int = 0) -> json:
    pass


@route_password.get(pass_routes['get_all'])
async def get_passwords_all() -> json:
    pass


@route_password.get(pass_routes['search'])
async def get_password_search(**kwargs) -> json:
    pass


@route_password.put(pass_routes['update'])
async def update_password(password: Password) -> json:
    pass


@route_password.delete(pass_routes['delete'])
async def delete_password(id: int = 0) -> json:
    pass
