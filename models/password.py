from pydantic import BaseModel
from typing import Optional


class Password(BaseModel):
    password_1: Optional[str] = None
    login_id: int = 0
