import json
from fastapi import APIRouter
from models.login import Login
from routes.routes import all_routes
from resource.login_resource import (
    create_login, get_login_by_id, get_logins_all,
    get_login_search, update_login, delete_login
)


route_login = APIRouter()
log_routes = all_routes['login']


@route_login.post(log_routes['new'])
async def post_login(login: Login) -> json:
    return create_login(login=login)


@route_login.get(log_routes['get_id'])
async def get_by_id_login(id: int = 0) -> json:
    return get_login_by_id(id=id)


@route_login.get(log_routes['get_all'])
async def get_all_logins(id: int = 0) -> json:
    return get_logins_all(id=id)


@route_login.get(log_routes['search'])
async def get_search_login(**kwargs) -> json:
    return get_login_search(kwargs)


@route_login.put(log_routes['update'])
async def put_login(login: Login) -> json:
    return update_login(login=login)


@route_login.delete(log_routes['delete'])
async def del_login(id: int = 0) -> json:
    return delete_login(id=id)
