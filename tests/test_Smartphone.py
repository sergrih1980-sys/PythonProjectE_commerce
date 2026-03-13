import pytest


def test_smartphone_init(product_smartphone):
    assert product_smartphone.name == "Xiaomi Redmi Note 11"
    assert product_smartphone.description == "1024GB, Синий"
    assert product_smartphone.price == 31000.0
    assert product_smartphone.quantity == 14
    assert product_smartphone.efficiency == 90.3
    assert product_smartphone.model == "Note 11"
    assert product_smartphone.memory == 1024
    assert product_smartphone.color == "Синий"


def test_smartphone_add_product(product_smartphone, product_smartphone2):
    """Тест сложения двух экземпляров Smartphone."""
    result = product_smartphone + product_smartphone2
    assert result == 31000.0 * 14 + 210000.0 * 8


def test_smartphone_add_error_product(product_smartphone,
                                      product_smartphone2):
    with pytest.raises(TypeError, match="Нельзя складывать смартфон "
                                        "с другим типом товара"):
        product_smartphone + 1
