from src.product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass

def test_print_mixin(capsys):
    # Тест для Product
    Product("Test Product", "Test description", 100, 10)
    out, err = capsys.readouterr()
    expected_product = "Product('Test Product', 'Test description', '100', 10)"
    assert out.strip() == expected_product

    # Очищаем буфер capsys перед следующим тестом
    capsys.readouterr()

    # Тест для Smartphone — передаём все 8 аргументов
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
    # Ожидаемая строка теперь содержит все 8 параметров
    expected_smartphone = (
        "Smartphone('Xiaomi Redmi Note 11', '1024GB, Синий', '31000.0', "
        "14, '90.3', 'Note 11', 1024, 'Синий')"
    )
    assert out.strip() == expected_smartphone