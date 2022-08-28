import json
from fastapi import APIRouter
from models.account import Account
from routes.routes import all_routes


route_account = APIRouter()
acc_routes = all_routes['account']


@route_account.post(acc_routes['new'])
async def create_account(account: Account) -> json:
    pass


@route_account.put(acc_routes['update'])
async def update_account(account: Account) -> json:
    pass


@route_account.delete(acc_routes['delete'])
async def delete_account(id: int = 0) -> json:
    pass
