from .item import Item


def test_create_item():
    item = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=10
    )
    assert item.name == "Laptop"
    assert item.description == "A high-performance laptop"
    assert item.price == 999.99
    assert item.quantity_in_stock == 10
