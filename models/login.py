from pydantic import BaseModel
from typing import Optional


class Login(BaseModel):
    notepad: Optional[str] = None
    account_id: int = 0
