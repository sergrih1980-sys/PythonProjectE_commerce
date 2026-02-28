

class Produkt:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

if __name__ == "__main__":
    produkt = Produkt("", "10", 10, "Produkt")
    print(produkt.name)
    print(produkt.description)
    print(produkt.price)