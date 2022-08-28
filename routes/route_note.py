import json
from fastapi import APIRouter
from models.note import Note
from routes.routes import all_routes


route_note = APIRouter()
note_routes = all_routes['note']


@route_note.post(note_routes['new'])
async def create_note(note: Note) -> json:
    pass


@route_note.get(note_routes['get_id'])
async def get_note_by_id(id: int = 0) -> json:
    pass


@route_note.get(note_routes['get_all'])
async def get_notes_all() -> json:
    pass


@route_note.get(note_routes['search'])
async def get_notes_search(**kwargs) -> json:
    pass


@route_note.put(note_routes['update'])
async def update_note(note: Note) -> json:
    pass


@route_note.delete(note_routes['delete'])
async def delete_note(id: int = 0) -> json:
    pass
