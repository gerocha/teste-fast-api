from dataclasses import dataclass

from stock.value_object.price import Price

@dataclass
class Item:
    name: str
    description: str
    price: Price
    quantity_in_stock: int

    @property
    def is_in_stock(self) -> bool:
        return self.quantity_in_stock > 0

    def __gt__(self, other):
        if not isinstance(other, Item):
            raise NotImplementedError
        return self.price > other.price

    def __sub__(self, other):
        if not isinstance(other, int):
            raise NotImplementedError

        if other > self.quantity_in_stock:
            raise ValueError("Cannot subtract more than available stock.")

        return Item(
                self.name,
                self.description,
                self.price,
                self.quantity_in_stock - other
            )
