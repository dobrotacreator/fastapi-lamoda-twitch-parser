from pydantic import BaseModel

from utils.base_model import BaseWithTimeModel


class Task(BaseModel):
    query: str


class Category(BaseWithTimeModel):
    id: int
    name: str


class Channel(BaseWithTimeModel):
    channel_name: str
    game_name: str
