from typing import List

from src.product import Product


class Category:
    name: str
    description: str
    total_quantity: int
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str,
                 products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products else []

        # Увеличиваем счётчик категорий при создании объекта
        Category.category_count += 1

        # Увеличиваем общий счётчик продуктов
        # на количество переданных в конструкторе
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов {total_quantity} шт"

    def get_product_count(self) -> int:
        """Возвращает количество продуктов в категории"""
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в список товаров и
        увеличивает счётчик продуктов на 1."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты "
                            "класса Product или его наследников")

        self.__products.append(product)
        # Увеличиваем глобальный счётчик продуктов
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        """Возвращает список продуктов в категории (исходные объекты)"""
        return self.__products

    def average_price(self) -> float:
        """
        Возвращает среднюю цену всех товаров в категории.

        Использует обработку исключений для предотвращения
         ошибки деления на ноль.
        В случае возникновения ошибки (пустой список товаров)
         возвращается 0.0.

        Returns:
            float: Средняя цена товаров или 0.0, если товаров нет.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            # Если len(self.__products) == 0
            return 0.0
