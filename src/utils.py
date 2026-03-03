

from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        # Увеличиваем глобальный счётчик на количество переданных продуктов
        Category.product_count += len(self.__products)


    def get_product_count(self):
        """Возвращает количество продуктов в категории"""
        return len(self.__products)


    def add_product(self, product):
        """
        Добавляет продукт в список товаров и увеличивает счётчик продуктов на 1.

        Параметры:
        product — продукт, который нужно добавить в категорию
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = []
        for product in self.__products:
            product_str.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return '\n'.join(product_str)  # Объединяем строки с переносом строки между ними

    @classmethod
    def new_product(cls, name, price, description, quantity):
        """Создаёт новый экземпляр Product"""
        product = Product(name, price, description, quantity)
        return product

