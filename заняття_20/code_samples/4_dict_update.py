contact = {
    "name": "Марія",
    "city": "Львів",
    "phone": "+380991234567",
    "points": [10, 11]
}

contact["city"] = "Київ"
contact["telegram"] = "@maria"
contact["points"].append(12)

print(f"{contact['name']} з міста {contact['city']}")
print(contact["points"])
print(max(contact["points"]))
print(contact["telegram"])
