## Словник і кортеж: оцінки учня
## Завдання: знайди 2 помилки

student = {
    "name": "Марко",
    "marks": (10, 11, 12)
}

student["marks"][0] = 12

average = sum(student["points"]) / len(student["marks"])

print(student["name"])
print(average)
