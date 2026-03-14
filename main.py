from src.category import Category
from src.product import Product
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

    # Создаём смартфоны
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

# Оптимизированный вывод информации о смартфонах
smartphones = [smartphone1, smartphone2, smartphone3]
for i, smartphone in enumerate(smartphones, 1):
    print(f"--- Смартфон {i} ---")
    print(f"Название: {smartphone.name}")
    print(f"Описание: {smartphone.description}")
    print(f"Цена: {smartphone.price} руб.")
    print(f"Количество: {smartphone.quantity} шт.")
    print(f"Эффективность: {smartphone.efficiency}%")
    print(f"Модель: {smartphone.model}")
    print(f"Память: {smartphone.memory} ГБ")
    print(f"Цвет: {smartphone.color}")
    print()

# Создаём газонную траву с корректными значениями germination_days (int)
try:
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        7,
        "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        5,
        "Темно-зеленый"
    )
except Exception as e:
    print(f"Ошибка при создании газонной травы: {e}")
    raise

# Вывод информации о газонной траве
grasses = [grass1, grass2]
for i, grass in enumerate(grasses, 1):
    print(f"--- Газонная трава {i} ---")
    print(f"Название: {grass.name}")
    print(f"Описание: {grass.description}")
    print(f"Цена: {grass.price} руб.")
    print(f"Количество: {grass.quantity} шт.")
    print(f"Страна производства: {grass.country}")
    print(f"Дни прорастания: {grass.germination_days}")  # исправлено: было germination_period
    print(f"Цвет: {grass.color}")
    print()

# Проверка сложения
smartphone_sum = smartphone1 + smartphone2
print(f"Сумма стоимости смартфонов: {smartphone_sum} руб.")

grass_sum = grass1 + grass2
print(f"Сумма стоимости газонной травы: {grass_sum} руб.")

# Проверка сложения объектов разных типов
try:
    invalid_sum = smartphone1 + grass1
except TypeError as e:
    print(f"Возникла ошибка TypeError при попытке сложения: {e}")
else:
    print("Не возникла ошибка TypeError при попытке сложения")

# Создание категорий с наследниками Product
category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

# Добавление продукта в категорию
category_smartphones.add_product(smartphone3)

# Вывод продуктов в категории смартфонов
print("Продукты в категории 'Смартфоны':")
for product in category_smartphones.products:
    print(f"- {product.name}, {product.price} руб., {product.quantity} шт.")
print()

print(f"Общее количество продуктов во всех категориях: {Category.product_count}")

# Попытка добавить некорректный объект
try:
    category_smartphones.add_product("Not a product")
except TypeError as e:
    print(f"Возникла ошибка TypeError при добавлении не продукта: {e}")
else:
    print("Не возникла ошибка TypeError при добавлении не продукта")