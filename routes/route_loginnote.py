import json
from fastapi import APIRouter
from models.loginnote import LoginNote
from routes.routes import all_routes
from resource.loginnote_resource import LoginNoteResource


route_loginnote = APIRouter()
loginnote_routes = all_routes['loginnote']
login_note_resource = LoginNoteResource()


@route_loginnote.post(loginnote_routes['new'])
async def post_login_note(loginote: LoginNote) -> json:
    return await login_note_resource.create_login_note(loginote=loginote)


@route_loginnote.get(loginnote_routes['get_id'])
async def get_by_id_login_note(id: int = 0) -> json:
    return await login_note_resource.get_login_note_by_id(id=id)


@route_loginnote.get(loginnote_routes['get_all'])
async def get_all_login_notes(id: int = 0) -> json:
    return await login_note_resource.get_login_notes_all(id=id)


@route_loginnote.get(loginnote_routes['search'])
async def get_search_login_note(**kwargs) -> json:
    return await login_note_resource.get_login_note_search(**kwargs)


@route_loginnote.put(loginnote_routes['update'])
async def put_login_note(loginnote: LoginNote, id: int = 0) -> json:
    return await login_note_resource.udpate_login_note(loginnote=loginnote, id=id)


@route_loginnote.delete(loginnote_routes['delete'])
async def del_login_note(id: int = 0) -> json:
    return await login_note_resource.delete_login_note(id=id)
