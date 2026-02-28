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
def categories():
    return Category(



    )
