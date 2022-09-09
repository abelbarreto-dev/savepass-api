import json
from typing import Generator
from models.loginnote import LoginNote
from crypter.encrypter import Encrypt
from crypter.decrypter import Decrypt


class LoginNoteResource:

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

    async def create_login_note(self, loginote: LoginNote) -> json:
        pass

    async def get_login_note_by_id(self, id: int = 0) -> json:
        pass

    async def get_login_notes_all(self, id: int = 0) -> json:
        pass

    async def get_login_note_search(self, **kwargs) -> json:
        pass

    async def udpate_login_note(self, loginnote: LoginNote) -> json:
        pass

    async def delete_login_note(self, id: int = 0) -> json:
        pass

    # utils methods

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
