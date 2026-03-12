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
    print(category1)  # Ожидаемый вывод: «Смартфоны, количество продуктов 13 шт.» (5 + 8)
    print()

    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
