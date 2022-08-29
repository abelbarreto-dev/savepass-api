import json
from fastapi import APIRouter
from models.loginnote import LoginNote
from routes.routes import all_routes
from resource.loginnote_resource import (
    create_login_note, get_login_note_by_id, get_login_notes_all,
    get_login_note_search, udpate_login_note, delete_login_note
)


route_loginnote = APIRouter()
loginnote_routes = all_routes['loginnote']


@route_loginnote.post(loginnote_routes['new'])
async def post_login_note(loginote: LoginNote) -> json:
    return create_login_note(loginote=loginote)


@route_loginnote.get(loginnote_routes['get_id'])
async def get_by_id_login_note(id: int = 0) -> json:
    return get_login_note_by_id(id=id)


@route_loginnote.get(loginnote_routes['get_all'])
async def get_all_login_notes(id: int = 0) -> json:
    return get_login_notes_all(id=id)


@route_loginnote.get(loginnote_routes['search'])
async def get_search_login_note(**kwargs) -> json:
    return get_login_note_search(kwargs)


@route_loginnote.put(loginnote_routes['update'])
async def put_login_note(loginnote: LoginNote) -> json:
    return udpate_login_note(loginnote=loginnote)


@route_loginnote.delete(loginnote_routes['delete'])
async def del_login_note(id: int = 0) -> json:
    return delete_login_note(id=id)
