## Файл і список рядків

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python\n")
    file.write("dict\n")
    file.write("file\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines[0])
print(lines[-1].strip())
print(len(lines))
