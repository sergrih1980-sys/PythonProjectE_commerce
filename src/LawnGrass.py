from src.product import Product


class LawnGrass(Product):
    """Класс газонной травы с дополнительными атрибутами."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_days: int,
        color: str
    ):
        """
        Инициализация газонной травы.

        Args:
            name: название товара
            description: описание
            price: цена за единицу
            quantity: количество на складе
            country: страна производства
            germination_days: дни прорастания
            color: цвет травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_days = germination_days
        self.color = color
