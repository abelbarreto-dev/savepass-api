import uvicorn
from fastapi import FastAPI
from routes.route_account import route_account
from routes.route_login import route_login
from routes.route_password import route_password
from routes.route_note import route_note
from routes.route_loginnote import route_loginnote


# creating api
app = FastAPI()


# loading routes
app.include_router(route_account)
app.include_router(route_login)
app.include_router(route_password)
app.include_router(route_note)
app.include_router(route_loginnote)


# handler
def handler() -> None:
    # server uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)


# main
if __name__ == '__main__':
    handler()
