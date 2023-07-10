from pydantic import BaseModel

from utils.base_model import BaseWithTimeModel


class Task(BaseModel):
    category_url: str


class Product(BaseWithTimeModel):
    name: str
    brand: str
    price: float
