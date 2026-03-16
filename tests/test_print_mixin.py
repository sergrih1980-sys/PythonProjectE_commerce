from src.product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass

def test_print_mixin(capsys):
    # Тест для Product
    Product("Test Product", "Test description", 100.0, 10)
    message = capsys.readouterr()

    # Ожидаемая строка теперь точно соответствует реальному формату вывода
    expected_product = "Product('Test Product', 'Test description', '100.0', 10)"
    assert message.out.strip() == expected_product

    # Очищаем буфер capsys перед следующим тестом
    capsys.readouterr()

    # Тест для Smartphone — все 8 аргументов
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
    message = capsys.readouterr()
    expected_smartphone = (
        "Smartphone('Xiaomi Redmi Note 11', '1024GB, Синий', '31000.0', "
        "14, '90.3', 'Note 11', 1024, 'Синий')"
    )
    assert message.out.strip() == expected_smartphone