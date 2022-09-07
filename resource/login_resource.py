import json
from models.login import Login
from controller.tools.checker import (
    username_checker, email_checker, tag_checker
)
from controller.exceptions.exceptions import (
    UsernameError, EmailError, TagError, IDError
)


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

    # utils methods

    def _checker_username(self, username: str) -> None:
        if not isinstance(username, str):
            raise UsernameError('username type must be string.')
        if not username_checker(username=username):
            raise UsernameError('username is invalid.')

    def _checker_email(self, email: str) -> None:
        if not isinstance(email, str):
            raise EmailError('email type must be string.')
        if not email_checker(email=email):
            raise EmailError('email is invalid.')

    def _checker_tag(self, tag: str) -> None:
        if not isinstance(tag, str):
            raise TagError('tag type must be string.')
        if not tag_checker(tag=tag):
            raise TagError('tag is invalid.')

    def _checker_account_id(self, account_id: int) -> None:
        if not isinstance(account_id, str):
            raise IDError('account_id type must be string.')
        if not account_id < 1:
            raise IDError('account_id must be positive.')
