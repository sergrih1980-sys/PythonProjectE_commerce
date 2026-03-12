from src.product import Product

class Smartphone(Product):
   def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
       super().__init__(name, description, price, quantity)
       self.efficiency = efficiency
       self.model = model
       self.memory = memory
       self.color = color


   def __add__(self, other) -> float:
       """Возвращает общую стоимость смартфонов на складе. Складывать можно только смартфоны."""
       if isinstance(other, Smartphone):
           return self.price * self.quantity + other.price * other.quantity
       raise TypeError("Нельзя складывать смартфон с другим типом товара")



