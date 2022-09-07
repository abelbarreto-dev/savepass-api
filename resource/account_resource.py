import json
from models.account import Account
from controller.tools.checker import (
    username_checker, password_checker,
    email_checker, mobile_checker,
)
from controller.exceptions.exceptions import (
    IDError, UsernameError,
    PasswordError, MobileError,
    MobileDataType, EmailError,
)


class AccountResource:

    async def create_account(self, account: Account) -> json:
        try:
            self._checker_data_mobile(mobile=account.mobile)
            self._checker_data_email(email=account.mobile)
            self._checker_get_login(
                username=account.username, password=account.passwd
            )
        except (
            UsernameError, PasswordError, MobileError,
            MobileDataType, EmailError
        ) as exc:
            pass

    async def get_account_login(self, username: str, password: str) -> json:
        try:
            self._checker_get_login(username=username, password=password)
        except (UsernameError, PasswordError) as exc:
            pass

    async def update_account(self, username: str, password: str, mobile: str) -> json:
        try:
            self._checker_get_login(username=username, password=password)
            self._checker_data_mobile(mobile=mobile)
        except (UsernameError, PasswordError, MobileError, MobileDataType) as exc:
            pass

    async def delete_account(self, id: int = 0) -> json:
        try:
            self._checker_delete(id=id)
        except IDError as ide:
            pass

    # util private methods

    def _checker_get_login(self, username: str, password: str) -> None:
        if not isinstance(username, str):
            raise UsernameError('username must be string.')
        elif not isinstance(password, str):
            raise PasswordError('password mut be string.')
        elif not username_checker(username=username) and not email_checker(email=username):
            raise UsernameError('username is invalid.')
        elif not password_checker(password=password):
            raise PasswordError('password is invalid.')

    def _checker_data_mobile(self, mobile: str) -> None:
        if not isinstance(mobile, str):
            raise MobileDataType('mobile data type invalid.')
        elif not mobile_checker(mobile=mobile):
            raise MobileError('mobile number invalid.')

    def _checker_data_email(self, email: str) -> None:
        if not isinstance(email, str):
            raise EmailError('e-mail type invalid.')
        if not email_checker(email=email):
            raise EmailError('e-mail is invalid.')

    def _checker_delete(self, id: int = 0) -> None:
        if not isinstance(id, int):
            raise IDError('id type invalid.')
        elif id < 1:
            raise IDError('id must be a positive number.')
