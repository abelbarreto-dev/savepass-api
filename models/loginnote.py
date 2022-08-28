from pydantic import BaseModel
from typing import Optional


class LoginNote(BaseModel):
    notepad: Optional[str] = None
    login_id: int = 0
