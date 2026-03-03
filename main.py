from src.utils import Category
from src.product import Product

if __name__ == "__main__":
    # Создаём продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        180000.0,
        "256GB, Серый цвет, 200MP камера",
        5
    )
    product2 = Product(
        "iPhone 15",
        210000.0,
        "512GB, Gray Space",
        8
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        31000.0,
        "1024GB, Синий",
        14
    )

    # Выводим информацию о продуктах
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
    print()

    # Создаём категорию с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Проверяем атрибуты категории
    print(category1.name == "Смартфоны")
    print(category1.description)
    print("Количество продуктов в категории:", len(category1.products))
    print("Всего категорий:", Category.category_count)
    print("Всего продуктов:", Category.product_count)
    print()

    # Создаём второй продукт и категорию
    product4 = Product(
        "55\" QLED 4K",
        123000.0,
        "Фоновая подсветка",
        7
    )
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    # Выводим информацию о второй категории
    print(category2.name)
    print(category2.description)
    print("Количество продуктов в категории:", category2.get_product_count())
    print(category2.products)
    print()

    # Выводим общие счётчики
    print("Всего категорий:", Category.category_count)
    print("Всего продуктов:", Category.product_count)
    print()

    # Демонстрация добавления продукта
    print("Продукты в категории 'Смартфоны' до добавления:")
    print(category1.products)

    category1.add_product(product4)
    print("\nПродукты в категории 'Смартфоны' после добавления:")
    print(category1.products)
    print("Общее количество продуктов:", Category.product_count)
    print()

    # Тестирование фабричного метода
    new_product = Category.new_product(
        "Samsung Galaxy S24",
        190000.0,
        "512GB, Чёрный, 200MP камера",
        3
    )
    print("Новый продукт через фабричный метод:")
    print(f"Название: {new_product.name}")
    print(f"Описание: {new_product.description}")
    print(f"Цена: {new_product.price}")
    print(f"Остаток: {new_product.quantity}")
    print()