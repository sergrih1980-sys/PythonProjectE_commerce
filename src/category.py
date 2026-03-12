from src.product import Product

class Category:
        name: str
        description: str
        products: list
        total_quantity: int
        category_count = 0
        product_count = 0

        def __init__(self, name, description, products=None):
            self.name = name
            self.description = description
            self.__products = products if products else []

            Category.category_count += 1
            # Увеличиваем глобальный счётчик на количество переданных продуктов
            Category.product_count += len(self.__products)

        def __str__(self):
            total_quantity = sum(product.quantity for product in self.__products)
            return f"{self.name}, количество продуктов {total_quantity} шт"

        def get_product_count(self):
            """Возвращает количество продуктов в категории"""
            return len(self.__products)

        def add_product(self, product):
            """
            Добавляет продукт в список товаров \
            и увеличивает  счётчик продуктов на 1

            Параметры:
            product — продукт, который нужно добавить в категорию
            """
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты класса Product или его наследников")
            self.__products.append(product)
            Category.product_count += 1

        @property
        def products(self):
            """Возвращает список строк с информацией о продуктах"""
            result = []
            for product in self.__products:
                result.append(f"{product.name}, {product.price} руб. \
                Остаток: {product.quantity} шт.")
            return result  # Возвращаем список
