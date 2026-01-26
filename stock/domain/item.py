from dataclasses import dataclass

from stock.value_object.price import Price

@dataclass
class Item:
    name: str
    description: str
    price: Price
    quantity_in_stock: int

    def __gt__(self, other):
        if not isinstance(other, Item):
            raise NotImplementedError
        return self.price > other.price

    def __sub__(self, other):
        if not isinstance(other, int):
            raise NotImplementedError
        return Item(
                self.name,
                self.description,
                self.price,
                self.quantity_in_stock - other
            )
