## Словник і зміна значень

student = {
    "name": "Оля",
    "points": [10, 11]
}

student["points"].append(12)
student["group"] = "Red"

print(student["name"])      # Оля
print(student["points"])    # [10, 11, 12]
print(student["group"])     # Red
