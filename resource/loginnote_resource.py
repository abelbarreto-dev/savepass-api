import json
from controller.tools.datasec import DataSec
from models.loginnote import LoginNote
from controller.exceptions.exceptions import IDError, LoginNoteError


class LoginNoteResource:

    def __init__(self):
        self._datasec_ = DataSec()

    @property
    def _datasec(self) -> DataSec:
        return self._datasec_

    async def create_login_note(self, loginote: LoginNote) -> json:
        try:
            self._checker_id(id=loginnote.login_id, name='login_id')
            self._checker_login_note(login_note=loginnote.notepad)
        except (LoginNoteError, IDError) as exc:
            pass
        notepad_encrypted = self._datasec.encrypter(loginnote.notepad)

    async def get_login_note_by_id(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as exc:
            pass

    async def get_login_notes_all(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id, name='login_id')
        except IDError as exc:
            pass

    async def get_login_note_search(self, **kwargs) -> json:
        for key in kwargs.keys():
            kwargs[key] = self._datasec.encrypter(kwargs[key])
        login_decrypted = self._datasec.decrypter()

    async def udpate_login_note(self, loginnote: LoginNote, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
            self._checker_id(id=loginnote.login_id, name='login_id')
            self._checker_login_note(login_note=loginnote.notepad)
        except (LoginNoteError, IDError) as exc:
            pass
        notepad_encrypted = self._datasec.encrypter(loginnote.notepad)

    async def delete_login_note(self, id: int = 0) -> json:
        try:
            self._checker_id(id=id)
        except IDError as ecv:
            pass

    # utils methods

    def _checker_login_note(self, login_note: str) -> None:
        if login_note is None:
            return None
        if not isinstance(login_note, str):
            raise LoginNoteError('login_note must be string.')
        if len(login_note) < 1:
            raise LoginNoteError('login_note invalid: empty string.')

    def _checker_id(self, id: int, name: str = 'id') -> None:
        if not isinstance(id, int):
            raise IDError(f'{name} type must be string.')
        if not id < 1:
            raise IDError(f'{name} must be positive.')
