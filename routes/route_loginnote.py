import json
from fastapi import APIRouter
from models.loginnote import LoginNote
from routes.routes import all_routes


route_loginnote = APIRouter()
loginnote_routes = all_routes['loginnote']


@route_loginnote.post(loginnote_routes['new'])
async def create_login_note(loginote: LoginNote) -> json:
    pass


@route_loginnote.get(loginnote_routes['get_id'])
async def get_login_note_by_id(id: int = 0) -> json:
    pass


@route_loginnote.get(loginnote_routes['get_all'])
async def get_login_notes_all() -> json:
    pass


@route_loginnote.get(loginnote_routes['search'])
async def get_login_note_search(**kwargs) -> json:
    pass


@route_loginnote.put(loginnote_routes['update'])
async def udpate_login_note(loginnote: LoginNote) -> json:
    pass


@route_loginnote.delete(loginnote_routes['delete'])
async def delete_login_note(id: int = 0) -> json:
    pass
