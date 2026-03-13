from src.product import Product


def test_product_init():
    """Тест корректной инициализации продукта."""
    product = Product(
        name="55\" QLED 4K",
        price=123000.0,
        quantity=7,
        description="Фоновая подсветка"
    )
    assert product.name == "55\" QLED 4K"
    assert product.price == 123000.0
    assert product.quantity == 7
    assert product.description == "Фоновая подсветка"


def test_price_setter_valid_price(valid_product):
    """Тест установки корректной цены."""
    valid_product.price = 200000.0
    assert valid_product.price == 200000.0


def test_get_total_value():
    product = Product("Смартфон", "Мобильный телефон", 1000.0, 5)
    assert product.get_total_value() == 5000.0  # 1000 × 5


def test_add_two_products():
    product1 = Product("Смартфон 1", "Описание", 1000.0, 5)
    product2 = Product("Смартфон 2", "Описание", 2000.0, 3)
    total = product1 + product2
    assert total == 11000.0  # (1000×5) + (2000×3) = 5000 + 6000
