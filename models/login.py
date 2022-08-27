from pydantic import BaseModel
from typing import Optional


class Login(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    account_id: int = 0
