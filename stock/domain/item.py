from dataclasses import dataclass

@dataclass
class Item:
    name: str
    description: str
    price: float
    quantity_in_stock: int
