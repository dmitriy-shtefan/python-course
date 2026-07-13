## Робота з файлами: with open
## Завдання: знайди 2 помилки

with open("lesson_notes.txt", "w", encoding="utf-8") as file:
    file.write("Python\n")
    file.write("Файли\n")

with open("lesson_notes.txt", "r", encoding="utf-8") as file:
    notes = file.readlines()

print(notes[0])


# 1. неправильний "режим" відкриття файлу при читанні
# 2. неправильне ім'я змінної