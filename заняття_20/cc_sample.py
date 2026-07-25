class Card:
    def __init__(self, owner, balance, is_active=True):
        self.owner = owner
        # приватний атрибут
        self.__balance = balance
        self.active = is_active

    def add_money(self, amount):
        # чи дозволено змінювати баланс?
        # чи кількість (amount) > 0?
        if amount <= 0:
            return False, "Некоректна сума для нарахування"

        if not self.active:
            return False, "Картка не активна"

        self.__balance += amount

        return True, ""

    def withdraw_money(self, amount):
        if amount <= 0:
            return False, "Некоректна сума для зняття"

        if self.__balance <= amount:
            return False, "Не вистачає коштів на рахунку."

        self.__balance -= amount

        return True, ""

    def transfer_to(self, other_card, amount):
        # 1. зняти гроші зі своєї карти
        status, error_msg = self.withdraw_money(amount)
        if status:
            # 2. додати ці гроші до іншої карти
            status, error_msg = other_card.add_money(amount)
            if not status:
                self.add_money(amount)
                print(f"ERROR: {error_msg}")
            else:
                print("SUCCESS")
        else:
            print(f"ERROR: {error_msg}")

    def show_balance(self):
        print(f"Власник карти: {self.owner}.")
        print(f"Поточний баланс: {self.__balance}.")



card1 = Card('Oleg', 100, False)

# публічна зміна балансу
print(card1.__balance)
print(card1.owner)

card1.add_money(50)
card1.show_balance()

card2 = Card('Alyona', 0)
card2.show_balance()

card1.transfer_to(card2, 50)

card1.show_balance()
card2.show_balance()
