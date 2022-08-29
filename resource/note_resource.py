import json
from models.note import Note


async def create_note(note: Note) -> json:
    pass


async def get_note_by_id(id: int = 0) -> json:
    pass


async def get_notes_all(id: int = 0) -> json:
    pass


async def get_notes_search(**kwargs) -> json:
    pass


async def update_note(note: Note) -> json:
    pass


async def delete_note(id: int = 0) -> json:
    pass
