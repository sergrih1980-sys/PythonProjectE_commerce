import pytest


def test_produkt_LawnGrass_init(produkt_LawnGrass):
    assert produkt_LawnGrass.name == "Газонная трава"
    assert produkt_LawnGrass.description == "Элитная трава для газона"
    assert produkt_LawnGrass.price == 500.0
    assert produkt_LawnGrass.quantity == 20
    assert produkt_LawnGrass.country == "Россия"
    assert produkt_LawnGrass.germination_days == 7
    assert produkt_LawnGrass. color == "Зеленый"


def test_produkt_LawnGrass_add_product(produkt_LawnGrass, produkt_LawnGrass2):
    """Тест сложения двух газонных трав"""
    result = produkt_LawnGrass + produkt_LawnGrass2
    assert result == 500.0 * 20 + 450.0 * 15


def test_produkt_LawnGrass_add_error_product(produkt_LawnGrass):
    with pytest.raises(TypeError, match="Нельзя складывать с объектом, "
                                        "не являющимся продуктом"):
        produkt_LawnGrass + "не газонная трава"
