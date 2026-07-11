## Список кортежів

scores = [
#    0         1
    ("Оля",    12),     # 0
    ("Максим", 10),     # 1
    ("Іра",    11)      # 2
]

total = 0

for name, point in scores:
    total += point
    # total = total + point

print(total)         # 33
print(scores[2][1])  # Іра

