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


def test_price_setter_negative_price(capfd):
    """Тест установки отрицательной цены."""
    product = Product("Test Phone", 1000.0, 5, "Test description")
    initial_price = product.price

    # Пытаемся установить отрицательную цену
    product.price = -50.0

    # Проверяем, что цена не изменилась
    assert product.price == initial_price

    # Перехватываем вывод
    out, err = capfd.readouterr()
    output_text = out + err  # Объединяем оба потока

    expected_message = "Цена не должна быть нулевая или отрицательная"
    assert expected_message in output_text, \
        f"Ожидалось сообщение: '{expected_message}'"
