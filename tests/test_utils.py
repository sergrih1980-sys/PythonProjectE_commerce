

def test_category_init(sample_category):
    assert sample_category.name == "Телевизоры"
    assert "высоким разрешением" in sample_category.description
    assert isinstance(sample_category.products, list)
    assert len(sample_category.products) > 0  # или конкретное число


