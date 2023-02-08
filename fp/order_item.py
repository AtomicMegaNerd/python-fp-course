class OrderItem:
    name: str = ""
    itemnumber: int = 0
    quantity: int = 0
    price: float = 0
    backorderd: bool = False

    def __init__(self, name, itemnumber, quantity, price, backorderd) -> None:
        self.name = name
        self.itemnumber = itemnumber
        self.quantity = quantity
        self.price = price
        self.backorderd = backorderd
