class Customer:
    name: str = ""
    address: str = ""
    enterprise: bool = False

    def __init__(self, name, address, enterprise) -> None:
        self.name = name
        self.address = address
        self.enterprise = enterprise

    @staticmethod
    def notify(cust, msg):
        print(f"Sending {msg} to {cust.name} at {cust.address}")
