from src.product import Product
from src.category import Category

if __name__ == "__main__":

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        18000.0,
        5
    )
    product2 = Product(
        "iPhone 15",
        "512GB, Gray Space",
        21000.0,
        8
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        15000.0,
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
        "Фоновая подсветка",
        123000.0,
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

    #  Выводим общие счётчики
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
    try:
        new_product = Product.new_product({
            'name': 'Samsung Galaxy S24',
            'price': 190000.0,
            'quantity': 3,
            'description': '512GB, Чёрный, 200MP камера'
        })
        print("Новый продукт через фабричный метод:")
        print(f"Название: {new_product.name}")
        print(f"Описание: {new_product.description}")
        print(f"Цена: {new_product.price}")
        print(f"Остаток: {new_product.quantity}")
    except ValueError as e:
        print(f"Ошибка при создании продукта: {e}")
    print()

    # Вывод информации о категориях с использованием __str__
    print("Информация о категории 'Смартфоны':")
    print(category1)
    print("\nИнформация о категории 'Телевизоры':")
    print(category2)

    # Создаём товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    # Складываем товары
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    total_sum = product1.get_total_value() + product2.get_total_value() + product3.get_total_value()
    print(f"Общая сумма всех товаров: {total_sum} руб.")

    category1 = Category(
        "Смартфоны",
        "Смартфоны для коммуникации и дополнительных функций",
        [product1, product2]
    )

    # проверка __str__ категории
    print(category1)  # Ожидаемый вывод: «Смартфоны, количество продуктов 13 шт» (5 + 8)
    print()
