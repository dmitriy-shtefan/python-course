## Області видимості: загальна сума
## Завдання: знайди 2 помилки

total = 0


def add_points(points):
    global total
    total += points
    return total


add_points(5)
add_points(3)

print(total)


# print(score) - немає змінної score
# total += - зміна локальної змінної до її створення