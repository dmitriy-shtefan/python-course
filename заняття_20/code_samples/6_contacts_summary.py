contacts = [
    {"name": "Андрій", "city": "Київ", "topics": ("Python", "Git"), "points": 12},
    {"name": "Марія", "city": "Львів", "topics": ("Python", "HTML"), "points": 10},
    {"name": "Данило", "city": "Київ", "topics": ("Git", "SQL"), "points": 9}
]

cities = set()
all_topics = set()
kyiv_names = []
total_points = 0

for contact in contacts:
    cities.add(contact["city"])
    all_topics.update(contact["topics"])
    total_points += contact["points"]

    if contact["city"] == "Київ":
        kyiv_names.append(contact["name"])

print(len(contacts))
print(cities)
print(all_topics)
print(kyiv_names)
print(total_points / len(contacts))
