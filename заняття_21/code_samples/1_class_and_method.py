class Coffee:
    def __init__(self):
        self.size = "середня"

    def describe(self):
        print(f"Кава: {self.size}")


latte = Coffee()

print(latte.size)      # І: "середня", Б: "середня"
latte.size = "велика"
latte.describe()       # Б: "Кава: велика"


