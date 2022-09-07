import json
from models.note import Note


class NoteResource:

    async def create_note(self, note: Note) -> json:
        pass

    async def get_note_by_id(self, id: int = 0) -> json:
        pass

    async def get_notes_all(self, id: int = 0) -> json:
        pass

    async def get_notes_search(self, **kwargs) -> json:
        pass

    async def update_note(self, note: Note) -> json:
        pass

    async def delete_note(self, id: int = 0) -> json:
        pass
