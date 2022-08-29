import json
from fastapi import APIRouter
from models.note import Note
from routes.routes import all_routes
from resource.note_resource import (
    create_note, get_note_by_id, get_notes_all,
    get_notes_search, update_note, delete_note
)


route_note = APIRouter()
note_routes = all_routes['note']


@route_note.post(note_routes['new'])
async def post_note(note: Note) -> json:
    return create_note(note=note)


@route_note.get(note_routes['get_id'])
async def get_by_id_note(id: int = 0) -> json:
    return get_note_by_id(id=id)


@route_note.get(note_routes['get_all'])
async def get_all_notes(id: int = 0) -> json:
    return get_notes_all(id=id)


@route_note.get(note_routes['search'])
async def get_search_notes(**kwargs) -> json:
    return get_notes_search(kwargs)


@route_note.put(note_routes['update'])
async def put_note(note: Note) -> json:
    return update_note(note=note)


@route_note.delete(note_routes['delete'])
async def del_note(id: int = 0) -> json:
    return delete_note(id=id)
