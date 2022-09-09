from typing import Generator
from crypter.encrypter import Encrypt
from crypter.decrypter import Decrypt


class DataSec:

    def __init__(self, password: str = 'password'):
        self._PASSWORD = password
        self._encrypt_ = Encrypt()
        self._decrypt_ = Decrypt()

    @property
    def _encrypt(self) -> Encrypt:
        return self._encrypt_

    @property
    def _decrypt(self) -> Decrypt:
        return self._decrypt_

    def encrypter(self, *args) -> Generator:
        return (
            self._encrypt.encrypt_word(word=word, passwd=self._PASSWORD)
            for word in args
        )

    def decrypter(self, *args) -> Generator:
        return (
            self._decrypt.decrypt_word(word=word, passwd=self._PASSWORD)
            for word in args
        )
