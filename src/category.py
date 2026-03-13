from src.product import Product
from typing import List

class Category:
    name: str
    description: str
    products: List[Product]
    total_quantity: int
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products else []

        Category.category_count += 1
        # Увеличиваем глобальный счётчик на количество переданных продуктов
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов {total_quantity} шт"

    def get_product_count(self) -> int:
        """Возвращает количество продуктов в категории"""
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в список товаров и увеличивает счётчик продуктов на 1.

        Параметры:
        product — продукт, который нужно добавить в категорию
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        """Возвращает список продуктов в категории (не форматированный)"""
        return self.__products
