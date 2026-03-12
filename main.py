from src.product import Product
from src.category import Category
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


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

    # Создание экземпляров смартфонов
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )

    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )

    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий"
    )

    # Вывод информации о смартфонах
    print("=== ИНФОРМАЦИЯ О СМАРТФОНАХ ===")
    print(f"Название: {smartphone1.name}")
    print(f"Описание: {smartphone1.description}")
    print(f"Цена: {smartphone1.price} руб.")
    print(f"Количество: {smartphone1.quantity} шт.")
    print(f"Производительность: {smartphone1.efficiency}")
    print(f"Модель: {smartphone1.model}")
    print(f"Память: {smartphone1.memory} GB")
    print(f"Цвет: {smartphone1.color}")
    print()

    print(f"Название: {smartphone2.name}")
    print(f"Описание: {smartphone2.description}")
    print(f"Цена: {smartphone2.price} руб.")
    print(f"Количество: {smartphone2.quantity} шт.")
    print(f"Производительность: {smartphone2.efficiency}")
    print(f"Модель: {smartphone2.model}")
    print(f"Память: {smartphone2.memory} GB")
    print(f"Цвет: {smartphone2.color}")
    print()

    print(f"Название: {smartphone3.name}")
    print(f"Описание: {smartphone3.description}")
    print(f"Цена: {smartphone3.price} руб.")
    print(f"Количество: {smartphone3.quantity} шт.")
    print(f"Производительность: {smartphone3.efficiency}")
    print(f"Модель: {smartphone3.model}")
    print(f"Память: {smartphone3.memory} GB")
    print(f"Цвет: {smartphone3.color}")
    print()

    # Создание экземпляров газонной травы
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый"
    )

    # Вывод информации о газонной траве
    print("=== ИНФОРМАЦИЯ О ГАЗОННОЙ ТРАВЕ ===")
    print(f"Название: {grass1.name}")
    print(f"Описание: {grass1.description}")
    print(f"Цена: {grass1.price} руб.")
    print(f"Количество: {grass1.quantity} шт.")
    print(f"Страна-производитель: {grass1.country}")
    print(f"Срок прорастания: {grass1.germination_period}")
    print(f"Цвет: {grass1.color}")
    print()

    print(f"Название: {grass2.name}")
    print(f"Описание: {grass2.description}")
    print(f"Цена: {grass2.price} руб.")
    print(f"Количество: {grass2.quantity} шт.")
    print(f"Страна-производитель: {grass2.country}")
    print(f"Срок прорастания: {grass2.germination_period}")
    print(f"Цвет: {grass2.color}")
    print()

    # Тестирование сложения товаров одного типа
    print("=== ТЕСТИРОВАНИЕ СЛОЖЕНИЯ ===")
    smartphone_sum = smartphone1 + smartphone2
    print(f"Общая стоимость смартфонов: {smartphone_sum} руб.")

    grass_sum = grass1 + grass2
    print(f"Общая стоимость газонной травы: {grass_sum} руб.")
    print()

    # Тестирование попытки сложения разных типов товаров
    print("=== ПОПЫТКА СЛОЖЕНИЯ РАЗНЫХ ТИПОВ ===")
    try:
        invalid_sum = smartphone1 + grass1
    except TypeError as e:
        print(f"Возникла ошибка TypeError: {e}")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")
    print()

    # Работа с категориями
    print("=== РАБОТА С КАТЕГОРИЯМИ ===")
    category_smartphones = Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
        [smartphone1, smartphone2]
    )

    category_grass = Category(
        "Газонная трава",
        "Различные виды газонной травы",
        [grass1, grass2]
    )

    print(f"Категория '{category_smartphones.name}': {category_smartphones}")
    print(f"Количество продуктов в категории: {category_smartphones.get_product_count()}")

    # Добавление нового смартфона в категорию
    category_smartphones.add_product(smartphone3)
    print(f"После добавления Xiaomi Redmi Note 11: {category_smartphones}")

    # Вывод списка продуктов в категории
    print("\nСписок продуктов в категории 'Смартфоны':")
    for product_info in category_smartphones.products:
        print(f"- {product_info}")

    print()
    print(f"Общее количество продуктов во всех категориях: {Category.product_count}")
    print()

    # Тестирование добавления некорректного объекта в категорию
    print("=== ПОПЫТКА ДОБАВЛЕНИЯ НЕКОРРЕКТНОГО ОБЪЕКТА ===")
    try:
        category_smartphones.add_product("Not a product")
    except TypeError as e:
        print(f"Возникла ошибка TypeError: {e}")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
