from dataclasses import dataclass

from stock.value_object.price import Price

@dataclass
class Item:
    name: str
    description: str
    price: Price
    quantity_in_stock: int
