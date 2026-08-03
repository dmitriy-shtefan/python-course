# Дано рядок із невалідним JSON: після останнього поля стоїть зайва кома.
import json

json_text = '''
{
    "name": "Anna",
    "age": 24,
}
'''

# декодувати рядок за допомогою:

data = json.loads(json_text)

try:
    data = json.loads(json_text)
except json.decoder.JSONDecodeError:
    print("Невалідний формат")



# Обробіть `json.decoder.JSONDecodeError`. У повідомленні виведіть:
# - зрозумілий текст про невалідний JSON;