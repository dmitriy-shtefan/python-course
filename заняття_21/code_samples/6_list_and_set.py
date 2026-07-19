class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def describe(self):
        return f"{self.name}: {', '.join(self.ingredients)}"


recipe = Recipe("Смузі", ["банан", "ягоди", "банан", "молоко", "ягоди"])


unique_ingredients = set(recipe.ingredients)

print(recipe.describe())
print(sorted(unique_ingredients))
print(len(unique_ingredients))
