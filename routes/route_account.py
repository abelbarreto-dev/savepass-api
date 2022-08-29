import json
from fastapi import APIRouter
from models.account import Account
from routes.routes import all_routes
from resource.account_resource import (
    create_account, update_account, delete_account
)


route_account = APIRouter()
acc_routes = all_routes['account']


@route_account.post(acc_routes['new'])
async def post_account(account: Account) -> json:
    return create_account(account=account)


@route_account.put(acc_routes['update'])
async def put_account(account: Account) -> json:
    return update_account(account=account)


@route_account.delete(acc_routes['delete'])
async def del_account(id: int = 0) -> json:
    return delete_account(id=id)
