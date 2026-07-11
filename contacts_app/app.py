import time
import streamlit as st
from files_db import load_contacts, save_contacts, make_contact_id
from validation import validate_email, validate_phone


def display_contact(contact):
    with st.expander(contact['name']):
        st.write(f"ID: {contact.get('id', 'N/A')}")
        st.write(f"Ім'я: {contact['name']}")
        st.write(f"Телефон: {contact['phone']}")
        st.write(f"Email: {contact['email']}")
        st.write(f"Місто: {contact['city']}")
        # contact.get('sex', 'N/A')
        # contact['sex']


def get_contact_form_data(contacts):
    cities = ('Київ', 'Полтава', 'Харків', 'Львів', 'Одеса', 'Дніпро')

    with st.form("contact_form"):
        st.subheader("Новий контакт")

        name = st.text_input(f"Ім'я:", placeholder="Введіть ваше ім'я")
        phone = st.text_input(f"Телефон:", "+380")
        email = st.text_input(f"Email:", placeholder="Введіть ваш email")
        city = st.selectbox(f"Місто:", cities)

        submitted = st.form_submit_button("Додати й зберегти")

    if submitted:
        phone_ok, phone_message = validate_phone(phone)
        email_ok, email_message = validate_email(email)

        if not phone_ok:
            return False, phone_message, {}

        if not email_ok:
            return False, email_message, {}

        contact = {
            "id": make_contact_id(contacts),
            "name": name,
            "phone": phone,
            "email": email,
            "city": city
        }
        return True, "", contact

    return False, "", {}


def delete_contact_by_id(contacts, contact_id):
    updated_contacts = []

    for contact in contacts:
        if contact.get("id") != contact_id:
            updated_contacts.append(contact)

    return updated_contacts


st.title('Список контактів')

contacts = load_contacts()


list_tab, add_tab, del_tab = st.tabs(["Мої Контакти", "Додати Контакт", "Видалити Контакт"])

with add_tab:
    is_success, error_message, contact = get_contact_form_data(contacts)

    if is_success:
        contacts.append(contact)
        save_contacts(contacts)
        st.success("Контакт збережено.")
    elif error_message:
        st.error(error_message)

with list_tab:
    st.subheader("Список контактів")
    if contacts:
        for contact in contacts:
            display_contact(contact)
    else:
        st.info("Поки що контактів немає.")

with del_tab:
    st.subheader("Видалення контакту")

    contact = st.selectbox(
        "Контакти",
        contacts,
        format_func=lambda contact: str(contact["id"]) + " - " + contact["name"]
    )

    if st.button("Видалити"):
        contacts = delete_contact_by_id(contacts, contact["id"])
        save_contacts(contacts)
        st.success("Контакт видалено")
        time.sleep(3)
        st.rerun()
