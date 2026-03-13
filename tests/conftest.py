import pytest

from src.category import Category
from src.LawnGrass import LawnGrass
from src.product import Product
from src.Smartphone import Smartphone


@pytest.fixture
def products():
    """Фикстура для продукта с корректными данными"""
    return Product(
        name="Samsung Galaxy S23 Ultra",
        price=180000.0,  # исправлено: float вместо str
        description="256GB, Серый цвет, 200MP камера",
        quantity=5,  # исправлено: int вместо str
    )


@pytest.fixture
def sample_product():
    """Фикстура для образца продукта"""
    return Product(
        name="55\" QLED 4K",
        price=123000.0,
        quantity=7,
        description="Фоновая подсветка"
    )


@pytest.fixture
def sample_category():
    """Фикстура для категории с двумя продуктами"""
    product1 = Product(
        name="Телевизор 4K",
        price=50000.0,
        quantity=3,
        description="4K, HDR"
    )
    product2 = Product(
        name="Телевизор 8K",
        price=120000.0,
        quantity=1,
        description="8K, OLED"
    )
    return Category(
        name="Телевизоры",
        description="Современные телевизоры с высоким разрешением",
        products=[product1, product2]
    )


@pytest.fixture
def multiple_categories():
    """Фикстура для списка категорий"""
    cat1 = Category(
        name="Телевизоры",
        description="Категория 1",
        products=[
            Product(
                name="TV1",
                price=50000.0,
                quantity=2,
                description="Desc1"
            )
        ]
    )
    cat2 = Category(
        name="Смартфоны",
        description="Категория 2",
        products=[
            Product(
                name="Phone1",
                price=70000.0,
                quantity=5,
                description="Desc2"
            )
        ]
    )
    return [cat1, cat2]


@pytest.fixture
def valid_product():
    """Фикстура для валидного продукта"""
    return Product(
        name="Test Product",
        price=100.0,
        quantity=10,
        description="Test description"
    )


@pytest.fixture
def product_with_negative_price():
    """Фикстура для продукта с отрицательной ценой"""
    return Product(
        name="Invalid Product",
        price=-50.0,
        quantity=5,
        description="Negative price"
    )


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category(
        name="Empty Category",
        description="No products",
        products=[]
    )


@pytest.fixture
def category_with_products(valid_product):
    """Фикстура для категории с продуктами"""
    products = [
        valid_product,
        Product(
            name="Another",
            price=150.0,
            quantity=7,
            description="Another"
        )
    ]
    return Category(
        name="Test Category",
        description="With products",
        products=products
    )


@pytest.fixture
def product_smartphone():
    """Фикстура для смартфона"""
    return Smartphone(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
        efficiency=90.3,
        model="Note 11",
        memory=1024,
        color="Синий"
    )


@pytest.fixture
def product_smartphone2():
    """Фикстура для смартфона"""
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space"
    )


@pytest.fixture
def produkt_LawnGrass1():
    """ Фикстура для газонной травы """
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )


@pytest.fixture
def produkt_LawnGrass2():
    """ Фикстура для газонной травы """
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-Зеленый"
    )
