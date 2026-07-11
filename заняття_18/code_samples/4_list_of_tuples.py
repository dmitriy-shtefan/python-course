## Список кортежів

scores = [
    ("Оля", 12),
    ("Максим", 10),
    ("Іра", 11)
]

total = 0

for name, point in scores:
    total += point

print(total)
print(scores[1][0])
