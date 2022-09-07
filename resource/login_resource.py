import json
from models.login import Login


class LoginResource:

    async def create_login(self, login: Login) -> json:
        pass

    async def get_login_by_id(self, id: int = 0) -> json:
        pass

    async def get_logins_all(self, id: int = 0) -> json:
        pass

    async def get_login_search(self, **kwargs) -> json:
        pass

    async def update_login(self, login: Login) -> json:
        pass

    async def delete_login(self, id: int = 0) -> json:
        pass
