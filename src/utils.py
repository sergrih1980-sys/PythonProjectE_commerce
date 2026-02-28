

class Category:
    name: str
    description: str
    products: list
    numbers_categories = 0
    numbers_products = 0

    def __init__(self, name, description, products ):
        self.name = name
        self.description = description
        self.products = products
        Category.numbers_products += len(products) if products else 0
        Category.numbers_categories += 1





if __name__ == "__main__":
    category = Category(
        name="",
        description="",
        products=[]
        numbers_categories=0

    )
    print(category.name)
    print(category.description)
    print(category.products)