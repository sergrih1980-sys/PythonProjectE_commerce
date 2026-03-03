import pytest

from src.product import Product
from src.utils import Category


@pytest.fixture
def products():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        price="180000.0",
        description="256GB, Серый цвет, 200MP камера",
        quantity="5",
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
    return Product("Test Product", 100.0, 10, "Test description")


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
