import streamlit as st


def display_contact(contact):
    st.write(f"Ім'я: {contact['name']}")
    st.write(f"Телефон: {contact['phone']}")
    st.write(f"Email: {contact['email']}")
    st.write(f"Місто: {contact['city']}")


def get_contact_form():
    cities = ['Київ', 'Полтава', 'Харків', 'Львів', 'Одеса', 'Дніпро']

    contact = {}

    name = st.text_input(f"Ім'я:", placeholder="Введіть ваше ім'я")
    phone = st.text_input(f"Телефон:", "+380")
    email = st.text_input(f"Email:", placeholder="Введіть ваш email")
    city = st.selectbox(f"Місто:", cities)

    if name and phone and email and city:
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "city": city
        }

    return contact


def save_contact(contact):
    with open('contacts.txt', 'a', encoding='utf-8') as file:
        text = ','.join(contact.values())
        file.write(text + '\n')
        st.write('Збережено!')



st.title('Словники в Python')

st.write('Вивчимо новий тип/структуру даних в Python')

# list (список)
students = ["Alina", "Natalia", "Eduard", "Irina", "Bogdan"]

# st.write(f"Студент зі списку: {students[0]}")

# dictionary (словник)
student = {
    "name": "Bogdan",
    "phone": 380991234567,
    "email": "bogdan@gmail.com",
    "city": "Poltava"
}

name = student.get('name', '')
st.write(f"Студент зі словника: {name}")

# display_contact(student)

new_student = get_contact_form()

save_clicked = st.button("Зберегти інформацію")

if save_clicked and new_student:
    save_contact(new_student)
elif save_clicked:
    st.write("Помилка: заповніть всі поля контактної форми!")


if st.button("Показати інформацію"):
    display_contact(student)
