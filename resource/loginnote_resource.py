import json
from models.loginnote import LoginNote


class LoginNoteResource:

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
