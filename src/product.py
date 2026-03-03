

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = None
        self.price = price
        self.quantity = quantity
        self.description = description

    @property
    def price(self):
        """Геттер для приватного атрибута __price"""
        return self.__price

    @price.setter
    def price(self, value):
        """
        Сеттер для атрибута price с проверкой корректности значения.

        Если цена ≤ 0, выводится сообщение об ошибке и значение не изменяется.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
