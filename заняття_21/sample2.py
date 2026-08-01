class Keyboard:
    def __init__(self, brand):
        self.brand = brand
        self.__esc_code = 111
        self.__enter_code = 132


keyboard1 = Keyboard("Vinga")
print(keyboard1.brand)

