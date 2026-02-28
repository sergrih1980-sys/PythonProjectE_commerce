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
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        product3=Product(
            name="Xiaomi Redmi Note 11",
            price=31000.0,
            quantity=14,
            description="1024GB, Синий"

        ))