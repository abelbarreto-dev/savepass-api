import json
from models.account import Account
from controller.tools.datasec import DataSec
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

    def __init__(self):
        self._datasec_ = DataSec()

    @property
    def _datasec(self) -> DataSec:
        return self._datasec_

    async def create_account(self, account: Account) -> json:
        try:
            self._checker_data_username(username=account.username)
            self._checker_data_email(email=account.email)
            self._checker_data_password(password=account.passwd)
            self._checker_data_mobile(mobile=account.mobile)
        except (
            UsernameError, PasswordError, MobileError,
            MobileDataType, EmailError
        ) as exc:
            pass
        data_encrypted = self._datasec.encrypter(
            account.username, account.email, account.passwd, account.mobile
        )

    async def get_account_login(self, username: str, password: str) -> json:
        try:
            self._checker_get_login(username=username, password=password)
        except (UsernameError, PasswordError) as exc:
            pass
        data_encrypted = self._datasec.encrypter(username, password)
        data_decrypted = self._datasec.decrypter()

    async def update_account(self, username: str, password: str, mobile: str) -> json:
        try:
            self._checker_get_login(username=username, password=password)
            self._checker_data_mobile(mobile=mobile)
        except (UsernameError, PasswordError, MobileError, MobileDataType) as exc:
            pass
        data_encrypted = self._datasec.encrypter(username, password, mobile)

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
            raise PasswordError('password must be string.')
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

    def _checker_data_username(self, username: str) -> None:
        if not isinstance(username, str):
            raise UsernameError('username type must be string.')
        if not username_checker(username=username):
            raise UsernameError('username is invalid.')

    def _checker_data_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise PasswordError('password type must be string.')
        if not password_checker(password=password):
            raise PasswordError('password is invalid.')

    def _checker_delete(self, id: int = 0) -> None:
        if not isinstance(id, int):
            raise IDError('id type invalid.')
        elif id < 1:
            raise IDError('id must be a positive number.')
