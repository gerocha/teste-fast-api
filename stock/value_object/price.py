class Price:
    def __init__(self, initval=None, name="var"):
        self.val = initval
        self.name = name

    def __set__(self, obj, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        setattr(obj, "val", value)

    def __get__(self, obj, obj_type=None) -> float:
        return getattr(obj, "val", 0.0)
