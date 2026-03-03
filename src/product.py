

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, price: float, quantity: int, description: str):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @property
    def price(self):
        """Геттер для приватного атрибута __price"""
        return self.__price

    @classmethod
    def new_product(cls, name, price, description, quantity):
        """Создаёт новый экземпляр Product"""
        product = Product(name, price, description, quantity)
        return product


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
