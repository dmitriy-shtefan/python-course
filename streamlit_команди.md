# Шпаргалка Streamlit

Коротка пам'ятка за прикладами з занять: перший Streamlit-додаток, layout, сторінки, форма контакту, JSON-збереження і CSV-експорт.

## 1. Запуск додатка

У терміналі перейти в папку з файлом і запустити:

```bash
streamlit run app.py
```

Якщо фінальна версія лежить в іншому файлі:

```bash
streamlit run main.py
```

Мінімальний файл:

```python
import streamlit as st

st.title("Мій перший додаток")
st.write("Привіт зі Streamlit!")
```

## 2. Базова структура файлу

```python
import streamlit as st

st.set_page_config(page_title="Назва сторінки", layout="wide")

st.title("Головний заголовок")
st.write("Звичайний текст або дані")
```

Важливо: `st.set_page_config()` краще писати на початку, до інших `st.title()`, `st.write()` тощо.

## 3. Текст і заголовки

```python
st.title("Великий заголовок")
st.header("Розділ")
st.subheader("Підрозділ")
st.write("Звичайний текст")
st.caption("Маленький підпис")
```

`st.write()` - універсальна команда. Вона може показувати текст, числа, списки, словники, таблиці.

```python
student = {
    "name": "Bogdan",
    "phone": 380991234567,
    "city": "Poltava",
}

st.write(student)
```

## 4. Повідомлення для користувача

```python
st.success("Все збережено.")
st.error("Сталася помилка.")
st.info("Поки що даних немає.")
st.warning("Перевірте введені дані.")
```

Приклад з проєкту:

```python
if name.strip() and phone.strip() and email.strip():
    st.success("Контакт збережено у contacts.json.")
else:
    st.error("Заповніть усі поля.")
```

## 5. Введення даних

### Текстове поле

```python
name = st.text_input("Ім'я")
email = st.text_input("Email", placeholder="Введіть ваш email")
phone = st.text_input("Телефон", value="+380")
```

### Число

```python
age = st.number_input("Вік", min_value=0, max_value=120, value=16)
```

### Вибір зі списку

```python
city = st.selectbox(
    "Місто",
    ["Київ", "Полтава", "Харків", "Львів", "Одеса", "Дніпро"]
)
```

### Галочка

```python
show_raw = st.checkbox("Показати таблицю", value=True)
```

### Повзунок

```python
rows = st.slider("Кількість рядків", 5, 100, 20)
```

## 6. Кнопки

Кнопка повертає `True` тільки в момент натискання:

```python
if st.button("Привітатися"):
    st.write("Привіт!")
```

Приклад з перевіркою імені:

```python
name = st.text_input("Введіть ім'я")

if st.button("Привітатися") and name:
    st.write(f"Привіт, {name}!")
```

## 7. Форми

Форма групує кілька полів. Код всередині форми виконується як звичайно, але обробка зазвичай відбувається після `st.form_submit_button()`.

```python
with st.form("contact_form"):
    st.subheader("Новий контакт")

    name = st.text_input("Ім'я")
    phone = st.text_input("Телефон", value="+380")
    email = st.text_input("Email")
    city = st.selectbox("Місто", ["Київ", "Полтава", "Харків", "Львів", "Одеса", "Дніпро"])

    submitted = st.form_submit_button("Додати і зберегти")

if submitted:
    if name.strip() and phone.strip() and email.strip():
        contact = {
            "name": name.strip(),
            "phone": phone.strip(),
            "email": email.strip(),
            "city": city,
        }
        st.write(contact)
    else:
        st.error("Заповніть усі поля.")
```

Навіщо `.strip()`:

```python
name.strip()
```

Це прибирає зайві пробіли на початку і в кінці рядка. Наприклад `"  Anna  "` стає `"Anna"`.

## 8. Sidebar

`st.sidebar` - панель зліва для налаштувань.

```python
with st.sidebar:
    st.header("Налаштування")
    rows = st.slider("Кількість рядків", 5, 100, 20)
    chart_type = st.selectbox("Тип графіка", ["Line", "Bar"])
    show_raw = st.checkbox("Показати таблицю", value=True)
```

Зручно тримати там фільтри, перемикачі, налаштування графіка або режиму роботи.

## 9. Layout: контейнери, колонки, вкладки

### Контейнер

```python
with st.container(border=True):
    st.title("Streamlit layout demo")
    st.write("Цей блок згрупований у st.container.")
```

### Колонки

```python
left, right = st.columns([2, 1])

with left:
    st.subheader("Графік")

with right:
    st.subheader("Метрики")
```

Для двох однакових колонок:

```python
left, right = st.columns(2)
```

Приклад з кнопками:

```python
left, right = st.columns(2)

with left:
    if st.button("Показати JSON"):
        st.json(contacts)

with right:
    if st.button("Експортувати в CSV"):
        export_contacts_to_csv(contacts, ["name", "phone", "email", "city"])
        st.success("Створено файл contacts.csv.")
```

### Вкладки

```python
tab_data, tab_about = st.tabs(["Дані", "Про приклад"])

with tab_data:
    st.subheader("Таблиця")

with tab_about:
    st.write("Тут можна тримати пояснення або додаткові графіки.")
```

## 10. Метрики, таблиці і графіки

### Метрика

```python
st.metric("Середній бал", 87)
st.metric("Рядків", rows)
```

### Таблиця

```python
st.dataframe(data, use_container_width=True)
```

### Графік

```python
st.line_chart(data, x="x", y="value")
st.bar_chart(data, x="x", y="value")
```

## 11. Expander

`st.expander()` ховає деталі під заголовком. Добре підходить для списку контактів.

```python
for contact in contacts:
    title = contact.get("name", "Контакт без імені")

    with st.expander(title):
        st.write(f"Ім'я: {contact.get('name', '')}")
        st.write(f"Телефон: {contact.get('phone', '')}")
        st.write(f"Email: {contact.get('email', '')}")
        st.write(f"Місто: {contact.get('city', '')}")
```

Чому `contact.get("name", "")`, а не `contact["name"]`:

```python
contact.get("name", "")
```

Якщо ключа немає, програма не впаде з помилкою, а поверне порожній рядок.

