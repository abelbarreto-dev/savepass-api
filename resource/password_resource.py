import json
from controller.tools.datasec import DataSec
from models.password import Password
from controller.exceptions.exceptions import IDError, PasswordError
from controller.tools.checker import password_checker


class PasswordResource:

    def __init__(self):
        self._datasec_ = DataSec()

    @property
    def _datasec(self) -> DataSec:
        return self._datasec_

    async def create_password(self, password: Password) -> json:
        try:
            self._checker_id(id=password.login_id, name='login_id')
            self._checker_data_password(password=password.password_1)
        except (IDError, PasswordError) as exc:
            pass
        encrypt_passwd = self._datasec.encrypter(password.password_1)

    async def get_password_by_id(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as exc:
            pass

    async def get_passwords_all(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id, name='login_id')
        except IDError as exc:
            pass

    async def get_password_search(self, **kwargs) -> json:
        for key in kwargs.keys():
            kwargs[key] = self._datasec.encrypter(kwargs[key])
        login_decrypted = self._datasec.decrypter()

    async def update_password(self, password: Password, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
            self._checker_id(id=password.login_id, name='login_id')
            self._checker_data_password(password=password.password_1)
        except (IDError, PasswordError) as exc:
            pass
        encrypted_passwd = self._datasec.encrypter(password.password_1)

    async def delete_password(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as exc:
            pass

    # utils methods

    def _checker_data_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise PasswordError('password type must be string.')
        if not password_checker(password=password):
            raise PasswordError('password is invalid.')

    def _checker_id(self, id: int, name: str = 'id') -> None:
        if not isinstance(id, int):
            raise IDError(f'{name} type must be string.')
        if not id < 1:
            raise IDError(f'{name} must be positive.')
