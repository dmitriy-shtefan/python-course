import json
import os

FILE_NAME = 'contacts.json'

# Створіть функцію save_contacts(contacts),
# яка зберігає список контактів у файл contacts.json


def save_contacts(contacts):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)


# Створіть функцію load_contacts(),
# яка читає контакти з файлу contacts.json

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        contacts = json.load(file)

    return contacts
