student = ("Оля", 16, "Python Red", [11, 10, 12])

name, age, group, marks = student
average_mark = sum(marks) / len(marks)

print(f"{name}, {age} років, група {group}")
print(marks)
print(average_mark)
