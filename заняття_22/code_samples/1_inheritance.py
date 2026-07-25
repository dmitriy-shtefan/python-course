class Human:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Мене звати {self.name}"


class Kid(Human):
    def scream(self):
        return "Аааааа!!!"


man = Kid("Саша")

print(man.name)
print(man.introduce())
print(man.scream())
