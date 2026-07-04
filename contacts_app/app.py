import streamlit as st
from files_db import load_contacts, save_contacts


def display_contact(contact):
    with st.expander(contact['name']):
        st.write(f"Ім'я: {contact['name']}")
        st.write(f"Телефон: {contact['phone']}")
        st.write(f"Email: {contact['email']}")
        st.write(f"Місто: {contact['city']}")


def get_contact_form_data():
    cities = ['Київ', 'Полтава', 'Харків', 'Львів', 'Одеса', 'Дніпро']

    with st.form("contact_form"):
        st.subheader("Новий контакт")

        name = st.text_input(f"Ім'я:", placeholder="Введіть ваше ім'я")
        phone = st.text_input(f"Телефон:", "+380")
        email = st.text_input(f"Email:", placeholder="Введіть ваш email")
        city = st.selectbox(f"Місто:", cities)

        submitted = st.form_submit_button("Додати й зберегти")

    if submitted:
        if name and phone and email and city:
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "city": city
            }
            return contact
        else:
            st.error("Заповніть усі поля.")

    return False


st.title('Список контактів')

contacts = load_contacts()

contact = get_contact_form_data()
if contact:
    contacts.append(contact)
    save_contacts(contacts)
    st.success("Контакт збережено.")

st.subheader("Список контактів")
if contacts:
    for contact in contacts:
        display_contact(contact)
else:
    st.info("Поки що контактів немає.")
