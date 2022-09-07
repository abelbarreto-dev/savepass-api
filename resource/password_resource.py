import json
from models.password import Password


class PasswordResource:

    async def create_password(self, password: Password) -> json:
        pass

    async def get_password_by_id(self, id: int = 0) -> json:
        pass

    async def get_passwords_all(self, id: int = 0) -> json:
        pass

    async def get_password_search(self, **kwargs) -> json:
        pass

    async def update_password(self, password: Password) -> json:
        pass

    async def delete_password(self, id: int = 0) -> json:
        pass
