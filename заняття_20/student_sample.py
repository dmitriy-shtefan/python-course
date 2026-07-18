
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print('Навчаюся...')


student1 = Student("Eduard", 32)
student2 = Student("Bogdan", 28)

print(student1.name)
student1.study()

