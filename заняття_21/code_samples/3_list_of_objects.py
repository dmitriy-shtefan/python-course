class Task:
    def __init__(self, title, status):
        self.title = title
        self.status = status

    def is_done(self):
        return self.status == "готово"


tasks = [
    Task("Повторити списки", "готово"),
    Task("Створити клас", "нова"),
    Task("Зробити вправу", "готово")
]


for task in tasks:
    if task.is_done():
        print(task.title)

print(len(tasks))
