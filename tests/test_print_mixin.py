from src.product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass

def test_print_mixin(capsys):
    Product("Test Product", "Test description", 100, 10)
    out, err = capsys.readouterr()
    expected_product = "Product('Test Product', 'Test description', 100, 10)"
    assert out.strip() == expected_product


    capsys.readouterr()

    Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий"
    )
    out, err = capsys.readouterr()
    expected_smartphone = (
        "Smartphone('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, "
        "14, 90.3, 'Note 11', 1024, 'Синий')"
    )
    assert out.strip() == expected_smartphone

