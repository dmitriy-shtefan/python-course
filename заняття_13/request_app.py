# Програма, яка працює як журнал:
#
# 1. Користувач вводить категорію справи.
# 2. Користувач вводить текст справи.
# 3. Програма зберігає запис у файл `requests.csv`.
# 4. Користувач може подивитися всі збережені записи.
# 5. Користувач може знайти записи за словом або категорією.

import os


def save_request(category, text):
    category = category.strip()
    text = text.strip()
    if os.path.exists('requests.csv'):
        param = 'a'
    else:
        param = 'w'

    if category == "" or text == "":
        print("Категорія і текст не повинні бути порожніми")
    else:
        result_line = f"{category},{text}\n"

        with open('requests.csv', param, encoding='utf-8') as file:
            file.write(result_line)

        print('Дані збережено!')


# вивести на екран пронумерований список заявок з файлу
def show_requests():
    with open('requests.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for number, line in enumerate(lines, start=1):
        print(str(number) + ". " + line.strip())


def find_word(word):
    with open('requests.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    found = False

    for line in lines:
        if word in line:
            print(line.strip())
            found = True

    if not found:
        print("Жодного запису з цим словом немає")


while True:
    print("1 - додати заявку")
    print("2 - показати всі заявки")
    print("3 - знайти запис за словом")
    print("4 - вихід")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        category = input("Введіть категорію: ")
        text = input("Введіть текст заявки: ")
        save_request(category, text)
    elif choice == "2":
        show_requests()
    elif choice == "3":
        word = input("Введіть слово для пошуку: ")
        find_word(word)
    elif choice == "4":
        print("До побачення")
        break
    else:
        print("Невідома команда")