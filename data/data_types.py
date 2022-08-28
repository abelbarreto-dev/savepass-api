from pydantic.dataclasses import dataclass
from typing import Optional, List


@dataclass
class Account:
    id: int = 0
    username: str
    email: str
    passwd: str
    mobile: Optional[str] = None


@dataclass
class Note:
    id: int = 0
    notepad: Optional[str] = None
    account_id: int = 0


@dataclass
class Password:
    id: int = 0
    password_1: Optional[str] = None
    login_id: int = 0


@dataclass
class LoginNote:
    id: int = 0
    notepad: Optional[str] = None
    login_id: int = 0


@dataclass
class Login:
    id: int = 0
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    tag: Optional[str] = None
    passwords: Optional[List[Password]] = None
    notes: Optional[List[LoginNote]] = None
    account_id: int = 0
