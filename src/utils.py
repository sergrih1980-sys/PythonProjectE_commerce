

class Category:
    name: str
    description: str
    products: list

    def __init__(self, name, description, products ):
        self.name = name
        self.description = description
        self.products = products

if __name__ == "__main__":
    category = Category(
        name="My Category",
        description="My description",
        products=[]
    )
    print(category.products)