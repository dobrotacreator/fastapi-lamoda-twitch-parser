from pydantic import BaseModel


class Task(BaseModel):
    category_url: str


class Product(BaseModel):
    name: str
    brand: str
    price: float
