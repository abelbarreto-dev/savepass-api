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
        try:
            self._checks_create_and_update(login=login)
            self._checker_id(id=login.account_id, name='account_id')
        except (
            UsernameError, EmailError, TagError, IDError
        ) as exc:
            pass

    async def get_login_by_id(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as exc:
            pass

    async def get_logins_all(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id, name='account_id')
        except IDError as exc:
            pass

    async def get_login_search(self, **kwargs) -> json:
        pass

    async def update_login(self, login: Login, id: int = 0) -> json:
        try:
            self._checker_id(id=login.account_id, name='account_id')
            self._checker_id(id=id)
            self._checks_create_and_update(login=login)
        except (
            IDError, UsernameError, EmailError, TagError
        ) as exc:
            pass

    async def delete_login(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as exc:
            pass

    # utils methods

    def _checks_create_and_update(self, login: Login) -> None:
        if login.username is not None:
            self._checker_username(username=login.username)
        elif login.email is not None:
            self._checker_email(email=login.email)
        elif login.tag is not None:
            self._checker_tag(tag=login.tag)

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

    def _checker_id(self, id: int, name: str = 'id') -> None:
        if not isinstance(id, int):
            raise IDError(f'{name} type must be string.')
        if not id < 1:
            raise IDError(f'{name} must be positive.')
