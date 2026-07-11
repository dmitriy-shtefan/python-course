## Словник і кортеж

products = {
    "apple": (3, 12),
    "banana": (2, 20)
}

count, price = products["apple"]
products["orange"] = (1, 30)

print(count * price)
print(products["orange"][1])
print(len(products))
