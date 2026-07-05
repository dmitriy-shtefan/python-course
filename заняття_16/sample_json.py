import json

data = [
    {'name': 'Оля', 'grade': 92},
    {'name': 'Іван', 'grade': 85},
]


# запис у файл
with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)


# читання з файлу
with open('user.json', encoding='utf-8') as file:
    data = json.load(file)

print(data[0]['name'], data[0]['grade'])
