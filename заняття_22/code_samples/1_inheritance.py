class Human:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Мене звати {self.name}"


class Kid(Human):
    def scream(self):
        return "Аааааа!!!"


man = Kid("Саша")

print(man.name)          # Саша
print(man.introduce())   # Мене звати Саша
print(man.scream())      # Аааааа!!!
