from pydantic import BaseModel


class Task(BaseModel):
    query: str


class Category(BaseModel):
    id: int
    name: str
    created_at: str = None


class Channel(BaseModel):
    channel_name: str
    game_name: str
    created_at: str = None
