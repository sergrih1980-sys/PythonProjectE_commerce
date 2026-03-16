from src.product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass

def test_print_mixin(capsys):
    # Тест для Product
    Product("Test Product", "Test description", 100, 10)
    out, err = capsys.readouterr()
    expected_product = "Product('Test Product', 'Test description', '100', 10)"
    assert out.strip() == expected_product

