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


def test_get_total_value(product_a, product_b, product_c):
    """Тест метода get_total_value()."""
    assert product_a.get_total_value() == 1000  # 100 × 10
    assert product_b.get_total_value() == 400   # 200 × 2
    assert product_c.get_total_value() == 250   # 50 × 5


def test_add_two_products(product_a, product_b):
    """Тест сложения двух товаров через __add__."""
    result = product_a + product_b
    expected = 100 * 10 + 200 * 2  # 1000 + 400 = 1400
    assert result == expected


