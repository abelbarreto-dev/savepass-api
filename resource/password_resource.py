import json
from models.password import Password


async def create_password(password: Password) -> json:
    pass


async def get_password_by_id(id: int = 0) -> json:
    pass


async def get_passwords_all(id: int = 0) -> json:
    pass


async def get_password_search(**kwargs) -> json:
    pass


async def update_password(password: Password) -> json:
    pass


async def delete_password(id: int = 0) -> json:
    pass
