import json
from fastapi import APIRouter
from models.account import Account
from routes.routes import all_routes
from resource.account_resource import AccountResource


route_account = APIRouter()
acc_routes = all_routes['account']
acc_resource = AccountResource()


@route_account.post(acc_routes['new'])
async def post_account(account: Account) -> json:
    return await acc_resource.create_account(account=account)


@route_account.get(acc_routes['login'])
async def get_account_login(username: str, password: str) -> json:
    return await acc_resource.get_account_login(
        username=username, password=password
    )


@route_account.put(acc_routes['update'])
async def put_account(username: str, password: str, mobile: str) -> json:
    return await acc_resource.update_account(
        username=username, password=password, mobile=mobile
    )


@route_account.delete(acc_routes['delete'])
async def del_account(id: int = 0) -> json:
    return await acc_resource.delete_account(id=id)
