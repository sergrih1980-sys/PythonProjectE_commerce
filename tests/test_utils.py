from src.product import Product
from  src.utils import Category

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
    assert Product.product_count >= 1
