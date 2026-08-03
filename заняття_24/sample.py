class NotEnoughBalance(Exception):
    pass


try:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))

    if a < b:
        raise NotEnoughBalance("a не повинно бути менше ніж b")

    res = a - b
except ValueError:
    print("Не виходить перетворити текст на число")
except ZeroDivisionError:
    print("Не можна ділити на 0")
except NotEnoughBalance as e:
    print("Недостатньо коштів")
except Exception as e:
    print("Невідома нам помилка: ", e)
else:
    print("a / b = ", res)
finally:
    print("Програму завершено")


