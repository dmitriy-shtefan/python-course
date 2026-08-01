class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: {self.price} грн"

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def final_price(self):
        return self.price - self.discount

book = DiscountedProduct("Книга", 500, 100)

print(book.describe())      # Книга: 500 грн
print(book.final_price())   # 400
