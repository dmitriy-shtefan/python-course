class Contact:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def short_info(self):
        return f"{self.name} — {self.city}"


contacts = {
    "оля": Contact("Оля", "Київ"),
    "марія": Contact("Марія", "Львів")
}


print(contacts["оля"].short_info())
contacts["марія"].city = "Одеса"
print(contacts["марія"].short_info())
print(sorted(contacts))
