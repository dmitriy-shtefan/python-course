## Словник і кортеж

products = {
    "apple": (3, 12),
    "banana": (2, 20)
}

count, price = products["apple"]
products["orange"] = (1, 30)

print(count * price)            # 36
print(products["orange"][1])    # 30
print(len(products))            # 3
