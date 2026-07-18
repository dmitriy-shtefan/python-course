'''student = "Оля", 16, "Python Red", [11, 10, 12]

name, age, group, marks = student


result = False, "Error"

result_status, result_text = result

if result_status:
    print("Result is True")
else:
    print("Result is False")
'''

a = tuple()
b = ("",)
c = (0,)
d = (False,)
e = (0, False, "")

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))

'''

average_mark = sum(marks) / len(marks)

print(f"{name}, {age} років, група {group}")   # Оля, 16 років, група Python Red
print(marks)                                   # [11, 10, 12]
print(average_mark)                            # 11
'''