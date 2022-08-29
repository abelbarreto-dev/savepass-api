import json
from models.login import Login


async def create_login(login: Login) -> json:
    pass


async def get_login_by_id(id: int = 0) -> json:
    pass


async def get_logins_all(id: int = 0) -> json:
    pass


async def get_login_search(**kwargs) -> json:
    pass


async def update_login(login: Login) -> json:
    pass


async def delete_login(id: int = 0) -> json:
    pass
