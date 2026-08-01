class Animal:
    def speak(self):
        print("...")


class Dog(Animal):
    def speak(self):
        print("Гав!")


class Cat(Animal):
    def speak(self):
        print("Няв!")


class Fish(Animal):
    def speak(self):
        print("")


animals = [Dog(), Cat(), Fish()]
for animal in animals:
    animal.speak()








def dog_speak():
    print("Гав!")


def cat_speak():
    print("Няв!")


def fish_speak():
    print("")


animals = [
    {"type": "cat"},
    {"type": "dog"},
    {"type": "fish"}
]

for animal in animals:
    if animal['type'] == 'cat':
        cat_speak()
    elif animal['type'] == 'dog':
        dog_speak()
    elif animal['type'] == 'fish':
        fish_speak()