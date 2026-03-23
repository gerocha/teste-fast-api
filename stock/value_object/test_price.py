from stock.value_object.price import Price


class Anom:
    price = Price()


def test_price_instance():
    obj1 = Anom()
    obj1.price = 100.0
    assert obj1.price == 100.0


def test_price_negative_value():
    obj2 = Anom()
    try:
        obj2.price = -50.0
    except ValueError as e:
        assert str(e) == "Price cannot be negative."
    else:
        assert False, "Expected ValueError for negative price"
