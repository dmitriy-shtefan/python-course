## Словник і функція

def get_average(student):
    marks = student["marks"]
    return sum(marks) / len(marks)


student = {
    "name": "Данило",
    "marks": [10, 11, 12]
}

print(student["name"])
print(get_average(student))
