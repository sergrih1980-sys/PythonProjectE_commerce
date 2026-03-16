from src.product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass

def test_print_mixin(capsys):
    Product("Test Product", "Test description", 100, 10)
    message, _ = capsys.readouterr()
    assert message.out.strip() ==  "Product('Test Product', 'Test description', '100', 10)"



