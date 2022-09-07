import json
from models.account import Account


class AccountResource:

    async def create_account(self, account: Account) -> json:
        pass

    async def update_account(self, account: Account) -> json:
        pass

    async def delete_account(self, id: int = 0) -> json:
        pass
