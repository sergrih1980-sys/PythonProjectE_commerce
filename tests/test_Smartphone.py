import pytest


def test_smartphone_init(product_smartphone1):
    assert product_smartphone1.name == "Xiaomi Redmi Note 11"
    assert product_smartphone1.description == "1024GB, Синий"
    assert product_smartphone1.price == 31000.0
    assert product_smartphone1.quantity == 14
    assert product_smartphone1.efficiency == 90.3
    assert product_smartphone1.model == "Note 11"
    assert product_smartphone1.memory == 1024
    assert product_smartphone1.color == "Синий"


def test_smartphone_add_product(product_smartphone1, product_smartphone2):
    """Тест сложения двух экземпляров Smartphone."""
    result = product_smartphone1 + product_smartphone2
    assert result == 180000.0 * 5 + 210000.0 * 8


def test_smartphone_add_error_product(product_smartphone1,
                                      product_smartphone2):
    with pytest.raises(TypeError, match="Нельзя складывать с объектом, "
                                        "не являющимся продуктом"):
        product_smartphone1 + 1
