from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int | None
    username: str
    about: str | None


@dataclass
class Post:
    id: int
    text: str


@dataclass
class PostFull:
    id: int | None
    text: str
    created_at: datetime
    author: User
