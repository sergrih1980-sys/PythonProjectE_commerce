from src.utils import Category
from src.product import Product

if __name__ == "__main__":
    # Создаём продукты с корректными типами данных (цена — число)
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        180000.0,
        5,
        "256GB, Серый цвет, 200MP камера"
    )
    product2 = Product(
        "iPhone 15",
        210000.0,
        8,
        "512GB, Gray Space"
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        31000.0,
        14,
        "1024GB, Синий"
    )

    # Выводим информацию о продуктах
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
    print()

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)
    print()

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
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
    print(len(category1.products))
    print(Category.category_count)  # Статический счётчик категорий
    print(category1.product_count)  # Количество продуктов в этой категории
    print()

    # Создаём второй продукт и категорию
    product4 = Product(
        "55\" QLED 4K",
        123000.0,
        7,
        "Фоновая подсветка"
    )
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    # Выводим информацию о второй категории
    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    for product_info in category2.products:
        print(product_info)
    print()

    # Выводим общие счётчики
    print("Всего категорий:", Category.category_count)
    print("Всего продуктов:", Category.product_count)
    print()

    # Демонстрация добавления продукта
    print("Продукты в категории 'Смартфоны' до добавления:")
    for product_info in category1.products:
        print(f"  - {product_info}")

    category1.add_product(product4)
    print("\nПродукты в категории 'Смартфоны' после добавления:")
    for product_info in category1.products:
        print(f"  - {product_info}")
    print("Количество продуктов в категории:", category1.product_count)
    print()

    # Тестирование фабричного метода
    new_product = Product.new_product(
        "Samsung Galaxy S24",
        190000.0,
        3,
        "512GB, Чёрный, 200MP камера"
    )
    print("Новый продукт через фабричный метод:")
    print(f"Название: {new_product.name}")
    print(f"Описание: {new_product.description}")
    print(f"Цена: {new_product.price}")
    print(f"Остаток: {new_product.quantity}")
    print()
