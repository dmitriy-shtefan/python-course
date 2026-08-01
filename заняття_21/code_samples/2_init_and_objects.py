class Student:
    def __init__(self, name, completed_topics):
        self.name = name
        self.completed_topics = completed_topics

    def is_ready_for_oop(self):
        return "функції" in self.completed_topics


student = Student("Оля", ("списки", "словники", "функції"))

print(student.name)                # Оля
print(student.completed_topics)    # ("списки", "словники", "функції")
print(student.is_ready_for_oop())  # Б: True
