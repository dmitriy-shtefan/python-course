name = "Alina"


def scope_test():
    global name

    print(name)

    name = "Irina"
    val = 1
    print(name)
    return name


value = scope_test()
print(value)
