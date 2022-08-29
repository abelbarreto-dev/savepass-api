import json
from models.loginnote import LoginNote


async def create_login_note(loginote: LoginNote) -> json:
    pass


async def get_login_note_by_id(id: int = 0) -> json:
    pass


async def get_login_notes_all(id: int = 0) -> json:
    pass


async def get_login_note_search(**kwargs) -> json:
    pass


async def udpate_login_note(loginnote: LoginNote) -> json:
    pass


async def delete_login_note(id: int = 0) -> json:
    pass

