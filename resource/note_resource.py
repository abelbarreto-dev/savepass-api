import json
from typing import Generator
from models.note import Note
from crypter.encrypter import Encrypt
from crypter.decrypter import Decrypt
from controller.exceptions.exceptions import NoteError, IDError


class NoteResource:

    PASSWORD = 'password'

    def __init__(self):
        self._encrypt = Encrypt()
        self._decrypt = Decrypt()

    @property
    def encrypt(self) -> Encrypt:
        return self._encrypt

    @property
    def decrypt(self) -> Decrypt:
        return self._decrypt

    async def create_note(self, note: Note) -> json:
        pass

    async def get_note_by_id(self, id: int = 0) -> json:
        pass

    async def get_notes_all(self, id: int = 0) -> json:
        pass

    async def get_notes_search(self, **kwargs) -> json:
        pass

    async def update_note(self, note: Note, id: int = 0) -> json:
        pass

    async def delete_note(self, id: int = 0) -> json:
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

    def _encrypter(self, *args) -> Generator:
        return (
            self.encrypt.encrypt_word(word=word, passwd=self.PASSWORD)
            for word in args
        )

    def _decrypter(self, *args) -> Generator:
        return (
            self.decrypt.decrypt_word(word=word, passwd=self.PASSWORD)
            for word in args
        )
