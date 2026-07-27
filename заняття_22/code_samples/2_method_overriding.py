class Message:
    def show(self):
        return "Нове повідомлення"


class Warning(Message):
    def show(self):
        return "Увага!"


message = Message()
warning = Warning()

print(message.show())    # Нове повідомлення
print(warning.show())    # Увага!
