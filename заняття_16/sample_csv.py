import csv

with open('sample.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['grade'])


orders = [
    {
        "id": 1,
        "products": [
            {
                "name": "Масло",
                "expiration_date": "2026-07-07"
            }
        ],
        "price": 100.0
    }
]


rows = [
    {'name': 'Оля', 'grade': 92},
    {'name': 'Іван', 'grade': 85},
]

with open('out2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'grade'])
    writer.writeheader()
    writer.writerows(rows)
