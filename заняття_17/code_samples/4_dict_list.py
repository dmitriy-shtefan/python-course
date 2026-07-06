## Список словників

contacts = [
    {"name": "Андрій", "city": "Київ"},
    {"name": "Марія", "city": "Львів"},
    {"name": "Данило", "city": "Київ"}
]

count = 0

for contact in contacts:
    if contact["city"] == "Київ":
        count += 1

print(count)                 # Е,А:2 (І:1)
print(contacts[1]["name"])   # Марія
