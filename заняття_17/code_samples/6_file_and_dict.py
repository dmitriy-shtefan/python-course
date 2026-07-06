## Файл і словник

with open("scores.txt", "w", encoding="utf-8") as file:
    file.write("Оля 12\n")
    file.write("Максим 10\n")
    file.write("Оля 11\n")

scores = {}

with open("scores.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        name = parts[0]
        point = parts[1]
        scores[name] = int(point)

print(scores)           # {'Оля': 11, 'Максим': 10}
print(scores["Оля"])    # 11
