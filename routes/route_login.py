import json
from fastapi import APIRouter
from models.login import Login
from routes.routes import all_routes


route_login = APIRouter()
log_routes = all_routes['login']


@route_login.post(log_routes['new'])
async def create_login(login: Login) -> json:
    pass


@route_login.get(log_routes['get_id'])
async def get_login_by_id(id: int = 0) -> json:
    pass


@route_login.get(log_routes['get_all'])
async def get_logins_all() -> json:
    pass


@route_login.get(log_routes['search'])
async def get_login_search(**kwargs) -> json:
    pass


@route_login.put(log_routes['update'])
async def update_login(login: Login) -> json:
    pass


@route_login.delete(log_routes['delete'])
async def delete_login(login: Login) -> json:
    pass
