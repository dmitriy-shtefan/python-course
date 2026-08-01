class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def describe(self):
        return f"{self.name}: {', '.join(self.ingredients)}"


recipe = Recipe("Смузі", ["банан", "ягоди", "банан", "молоко", "ягоди"])


unique_ingredients = set(recipe.ingredients)

print(recipe.describe())           # Смузі: "банан", "ягоди", "банан", "молоко", "ягоди"
print(sorted(unique_ingredients))  # банан, молоко, ягоди
print(len(unique_ingredients))     # 3
