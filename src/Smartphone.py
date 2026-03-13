from src.product import Product


class Smartphone(Product):
    """Класс смартфона с дополнительными атрибутами."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ):
        """
        Инициализация смартфона.

        Args:
            name: название товара
            description: описание
            price: цена за единицу
            quantity: количество на складе
            efficiency: эффективность (в %)
            model: модель смартфона
            memory: объём памяти (ГБ)
            color: цвет корпуса
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

def __add__(self, other) -> float:
    """Возвращает общую стоимость смартфонов на складе. Складывать можно только смартфоны."""
    if isinstance(other, Smartphone):
        return (
                self.price * self.quantity +
                other.price * other.quantity
        )
    raise TypeError("Нельзя складывать смартфон с другим типом товара")