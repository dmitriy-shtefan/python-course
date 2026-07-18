tasks = [
    {"title": "Повторити списки", "status": "готово", "points": 10},
    {"title": "Вивчити множини", "status": "нова", "points": 0},
    {"title": "Зробити вправу", "status": "нова", "points": 8}
]

new_tasks = 0
total_points = 0

for task in tasks:
    if task["status"] == "нова":
        new_tasks += 1
    total_points += task["points"]

print(new_tasks)
print(total_points)

for task in tasks:
    if task["points"] >= 8:
        print(task["title"])
