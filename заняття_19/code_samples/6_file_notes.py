## Робота з файлами: with open
## Завдання: знайди 2 помилки

with open("lesson_notes.txt", "w", encoding="utf-8") as file:
    file.write("Python\n")
    file.write("Файли\n")

with open("lesson_notes.txt", "w", encoding="utf-8") as file:
    notes = file.readlines()

print(lines[0])
