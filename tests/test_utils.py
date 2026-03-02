
from src.utils import Category


def test_category_init(sample_category):
    assert sample_category.name == "Телевизоры"
    assert "высоким разрешением" in sample_category.description
    assert isinstance(sample_category.products, list)
    assert len(sample_category.products) > 0  # или конкретное число


def test_category_counter(sample_category):
    # Проверяем, что счётчик категорий увеличился
    assert Category.category_count >= 1


def test_produkt_counter(sample_product):
    # Проверяем счётчик продуктов
    assert Category.product_count >= 1


def test_products_property_empty_category(empty_category):
    """Тест свойства products для пустой категории."""
    result = empty_category.products

    assert isinstance(result, list), "Результат должен быть списком"
    assert len(result) == 0, \
        "В пустой категории список продуктов должен быть пустым"
