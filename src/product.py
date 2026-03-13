

class Product:
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def get_total_value(self) -> float:
        """Возвращает стоимость всех единиц товара на складе (цена × количество)."""
        return self.price * self.quantity

    def __add__(self, other) -> float:
        """
        Возвращает общую стоимость двух товаров на складе.
        Складывать можно только объекты класса Product или его наследников.
        """
        if not isinstance(other, Product):
            raise TypeError("Нельзя складывать с объектом, не являющимся продуктом")
        return self.price * self.quantity + other.price * other.quantity


    @property
    def price(self) -> float:
        """Геттер для приватного атрибута __price"""
        return self.__price


    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        """Создаёт новый экземпляр Product из словаря с данными"""
        product = cls(**product_data)
        return product


    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для атрибута price с проверкой корректности значения."""
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = float(value)