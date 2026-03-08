

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def get_total_value(self) -> float:
        """Возвращает стоимость всех единиц
        товара на складе (цена × количество)."""
        return self.price * self.quantity

    def __add__(self, other) -> float:
        """ Возвращает общую стоимость всех товаров на складе. """
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        """Геттер для приватного атрибута __price"""
        return self.__price

    @classmethod
    def new_product(cls, product_data: dict):
        """ Создаёт новый экземпляр Product из словаря с данными """
        product = cls(**product_data)
        return product

    @price.setter
    def price(self, value: float):
        """
        Сеттер для атрибута price с проверкой корректности значения.

        Если цена ≤ 0, выводится сообщение об ошибке и значение не изменяется.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(value)
