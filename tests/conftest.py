import pytest

from src.product import Product
from src.category import Category
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


@pytest.fixture
def products():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        price=180000.0,
        description="256GB, Серый цвет, 200MP камера",
        quantity=5
    )


@pytest.fixture
def sample_product():
    return Product(
        name="55\" QLED 4K",
        price=123000.0,
        quantity=7,
        description="Фоновая подсветка"

    )


@pytest.fixture
def sample_category():
    product1 = Product("Телевизор 4K", 50000.0, 3, "4K, HDR")
    product2 = Product("Телевизор 8K", 120000.0, 1, "8K, OLED")

    return Category(
        name="Телевизоры",
        description="Современные телевизоры с высоким разрешением",
        products=[product1, product2]
    )


@pytest.fixture
def multiple_categories():
    cat1 = Category(
        "Телевизоры",
        "Категория 1",
        [Product("TV1", 50000.0, 2, "Desc1")]
    )
    cat2 = Category(
        "Смартфоны",
        "Категория 2",
        [Product("Phone1", 70000.0, 5, "Desc2")]

    )
    return [cat1, cat2]


@pytest.fixture
def valid_product():
    """Фикстура для валидного продукта"""
    return Product("Test Product", "Test description", 100, 10)


@pytest.fixture
def product_with_negative_price():
    """Фикстура для продукта с отрицательной ценой"""
    return Product("Invalid Product", -50.0, 5, "Negative price")


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category("Empty Category", "No products", [])


@pytest.fixture
def category_with_products(valid_product):
    """Фикстура для категории с продуктами"""
    products = [valid_product, Product("Another", 150.0, 7, "Another")]
    return Category("Test Category", "With products", products)


@pytest.fixture
def product_smartphone1():
    return Smartphone("Xiaomi Redmi Note 11",
    "1024GB, Синий",
    31000.0,
    14,
    90.3,
    "Note 11",
    1024,
    "Синий"
)


@pytest.fixture
def product_smartphone2():
    return Smartphone("Iphone 15",
    "512GB, Gray space",
    210000.0,
    8,
    98.2,
    "15",
    512,
    "Gray space"
)


@pytest.fixture
def produkt_LawnGrass1():
    return LawnGrass("Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        7,
        "Зеленый"
    )


@pytest.fixture
def produkt_LawnGrass2():
    return LawnGrass("Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        5,
        "Темно-зеленый"
    )
