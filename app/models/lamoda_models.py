from pydantic import BaseModel


class Product(BaseModel):
    name: str
    brand: str
    price: float
