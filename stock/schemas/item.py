from pydantic import BaseModel


class ItemSchema(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int
