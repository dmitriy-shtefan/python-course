# Як запустити Streamlit-застосунок у Windows

Ця інструкція допоможе запустити будь-який Streamlit-проєкт навіть якщо ви робите це вперше.

---

# Крок 1. Відкрийте термінал

Є два прості способи.

## Варіант 1. У PyCharm (рекомендовано)

1. Відкрийте свій проєкт.
2. Внизу вікна натисніть **Terminal**.

Якщо вкладки **Terminal** не видно:

* натисніть **View → Tool Windows → Terminal**

Відкриється чорне (або біле) вікно, куди можна вводити команди.

---

## Варіант 2. PowerShell

1. Відкрийте меню **Пуск**.
2. Введіть **PowerShell**.
3. Запустіть програму **Windows PowerShell**.

---

# Крок 2. Перевірте, чи ви знаходитесь у правильній папці

Введіть команду:

```powershell
dir
```

Ви побачите список файлів і папок.

Шукайте серед них:

* `main.py`
* `app.py`
* `streamlit_app.py`
* папку `venv`

Наприклад:

```
main.py
requirements.txt
venv
data.csv
```

Це означає, що ви відкрили папку вашого проєкту.

---

# Крок 3. Якщо ви не в тій папці

Подивіться, де ви зараз знаходитеся:

```powershell
pwd
```

Приклад:

```
C:\Users\Ivan
```

Якщо потрібно перейти в іншу папку, використовуйте команду

```powershell
cd НазваПапки
```

Наприклад

```powershell
cd Documents
```

ще раз

```powershell
cd PythonProjects
```

ще раз

```powershell
cd MyStreamlitApp
```

Тепер перевірте вміст папки:

```powershell
dir
```

---

## Якщо потрібно повернутися на один рівень назад

```powershell
cd ..
```

Наприклад:

```
Було:
C:\Users\Ivan\Documents\PythonProjects

Після команди cd ..

Стало:
C:\Users\Ivan\Documents
```

---

# Крок 4. Перевірте, чи є віртуальне середовище (venv)

У папці проєкту виконайте

```powershell
dir
```

Якщо бачите папку

```
venv
```

або

```
.venv
```

— усе добре.

Наприклад:

```
main.py
requirements.txt
venv
```

---

# Крок 5. Активуйте віртуальне середовище

Якщо папка називається **venv**:

```powershell
venv\Scripts\activate
```

Якщо папка називається **.venv**:

```powershell
.venv\Scripts\activate
```

Після успішної активації на початку рядка з'явиться назва середовища.

Наприклад:

```
(venv) PS C:\Users\Ivan\MyProject>
```

Якщо бачите `(venv)` або `(.venv)` — усе працює правильно.

---

# Крок 6. Запустіть Streamlit

Потрібно вказати файл, з якого починається програма.

Найчастіше це:

```
main.py
```

або

```
app.py
```

або

```
streamlit_app.py
```

Запуск виглядає так:

```powershell
python -m streamlit run main.py
```

або

```powershell
python -m streamlit run app.py
```

або

```powershell
python -m streamlit run streamlit_app.py
```

---

# Як зрозуміти, який файл запускати?

Подивіться список файлів:

```powershell
dir
```

Приклад:

```
app.py
main.py
utils.py
database.py
requirements.txt
```

Тоді запускаємо

```powershell
python -m streamlit run app.py
```

Якщо бачите

```
main.py
```

то запускаємо

```powershell
python -m streamlit run main.py
```

Запускати потрібно **той файл, у якому написаний Streamlit-код** (наприклад, є рядок `import streamlit as st`).

---

# Якщо все успішно

У терміналі з'явиться приблизно таке повідомлення:

```
Local URL: http://localhost:8501
```

Через кілька секунд браузер відкриється автоматично.

Якщо цього не сталося, просто відкрийте браузер і перейдіть за адресою:

```
http://localhost:8501
```

---

# Найкоротша пам'ятка

```powershell
dir                     # подивитися файли

cd НазваПапки           # перейти в папку

cd ..                   # повернутися назад

venv\Scripts\activate   # активувати venv

python -m streamlit run app.py    # запустити програму
```

Якщо якась команда не працює, уважно прочитайте текст помилки — у більшості випадків він підказує, що саме потрібно виправити.
