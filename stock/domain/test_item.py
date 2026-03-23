from .item import Item


def test_create_item():
    item = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=10,
    )
    assert item.name == "Laptop"
    assert item.description == "A high-performance laptop"
    assert item.price == 999.99
    assert item.quantity_in_stock == 10


def test_item_comparison():
    item1 = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=10,
    )
    item2 = Item(
        name="Tablet",
        description="A lightweight tablet",
        price=499.99,
        quantity_in_stock=20,
    )
    assert item1 > item2


def test_item_subtraction():
    item = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=10,
    )
    updated_item = item - 3
    assert updated_item.quantity_in_stock == 7
    assert updated_item.name == item.name
    assert updated_item.description == item.description
    assert updated_item.price == item.price


def test_item_subtraction_invalid():
    item = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=10,
    )
    try:
        item - "3"
    except NotImplementedError:
        pass
    else:
        assert False, "Expected NotImplementedError for invalid subtraction type"


def test_item_subtraction_exceeding_stock():
    item = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=10,
    )
    try:
        item - 15
    except ValueError as e:
        assert str(e) == "Cannot subtract more than available stock."
    else:
        assert False, "Expected ValueError for exceeding stock subtraction"


def test_item_is_in_stock():
    item = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=5,
    )
    assert item.is_in_stock is True

    item_out_of_stock = Item(
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity_in_stock=0,
    )
    assert item_out_of_stock.is_in_stock is False
