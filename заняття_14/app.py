import streamlit as st


def day_14():
    # header
    # h1, h2, h3, ... h6

    st.title('Знайомство з Streamlit')   # h1
    st.subheader('Заняття 14')  # h3

    # wrtite - вивід простого тексту
    st.write('Сьогодні розглянемо як писати програми з Streamlit')

    # input - універсальне поле для вводу (текстове)
    first_name = st.text_input('Ім\'я:').strip()

    # button - кнопка
    clicked = st.button("Привітатися")

    if clicked and first_name:
        st.write(f"Привіт, {first_name}!")

    # textarea - для вводу тексту (з великою довжиною)
    st.text_area('Опис курсу')

    # select - список
    st.selectbox('Оберіть мову', ['Python', 'Java'])

    # checkbox - [v] [v] [ ]
    st.checkbox('Я приймаю умови користування')

    # radio button - (*) ( ) ( )
    st.radio('Оберіть швидкіть',
             ['Низька', 'Середня', 'Висока'])


def day_14_task():
    # Створіть текстовий аналізатор.
    # Додайте поле:
    #
    # message = st.text_input("Введіть повідомлення")
    #
    # Покажіть:
    # - саме повідомлення;
    # - кількість символів;
    # - повідомлення у нижньому регістрі.

    st.title("Завдання 14.1")
    message = st.text_input("Введіть повідомлення")

    if message:
        st.write(f"Повідомлення: '{message}'")

        message_len = len(message)
        st.write(f"Кількість символів: {message_len}")

        message_lower = message.lower()
        st.write(f"Повідомлення в нижньому регістрі: '{message_lower}'")







day_14_task()

