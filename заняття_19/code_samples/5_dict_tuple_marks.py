## Словник і кортеж: оцінки учня
## Завдання: знайди 2 помилки

student = {
    "name": "Марко",
    "marks": [10, 11, 12]
}

student["marks"][0] = 12

average = sum(student["marks"]) / len(student["marks"])

print(student["name"])
print(average)


# 1. marks повинно бути списком
# 2. неправильний ключ в словнику