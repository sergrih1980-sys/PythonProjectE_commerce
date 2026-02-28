import pytest
from src.product import Product



def test_product_init(sample_product):
    assert sample_product.name == "55\" QLED 4K"
    assert sample_product.price == 123000.0
    assert sample_product.quantity == 7
    assert "Фоновая подсветка" in sample_product.description

