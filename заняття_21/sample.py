class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        # захищений (protected)
        self._id = id

    def introduce(self):
        print(f"Мене звати {self.name}. Мені {self.age} роки(ів)")


class Student(Person):

    def __init__(self, name, age, id, group, course):
        super().__init__(name, age, id)
        self.group = group
        self.course = course

    def study(self):
        print("Навчаюся")
        print(self._id)


class Teacher:
    def __init__(self, name, age, id, specialization):
        super().__init__(name, age, id)
        self.specialization = specialization


student = Student("Максим", 33, "ТЧХУ", "Python")
student.introduce()
