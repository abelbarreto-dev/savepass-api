from pydantic import BaseModel
from typing import Optional


class Account(BaseModel):
    username: str
    email: str
    passwd: str
    mobile: Optional[str] = None
