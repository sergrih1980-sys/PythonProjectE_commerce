import pytest


def test_produkt_LawnGrass_init(produkt_LawnGrass1):
    assert produkt_LawnGrass1.name == "Газонная трава"
    assert produkt_LawnGrass1.description == "Элитная трава для газона"
    assert produkt_LawnGrass1.price == 500.0
    assert produkt_LawnGrass1.quantity == 20
    assert produkt_LawnGrass1.country =="Россия"
    assert produkt_LawnGrass1.germination_period == "7 дней"
    assert produkt_LawnGrass1. color == "Зеленый"


def test_produkt_LawnGrass_add_product(produkt_LawnGrass1, produkt_LawnGrass2):
    """Тест сложения двух газонных трав"""
    result = produkt_LawnGrass1 + produkt_LawnGrass2
    assert result == 500.0 * 20 + 450.0 * 15


def test_produkt_LawnGrass_add_error_product(produkt_LawnGrass1, produkt_LawnGrass2):
    with pytest.raises(TypeError, match="Нельзя складывать газонную траву с другим типом товара"):
        produkt_LawnGrass1 + 1



