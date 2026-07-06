contact_pair = ("Olena", "+380998887766", 12, 40)
'''
print(contact_pair)

print("name: " + contact_pair[0])
print("phone: " + contact_pair[1])
print("age: " + str(contact_pair[-1]))

name, phone, grade, age = contact_pair


x, y = 2, 4

print(x, y)
'''

contact_pair = "Valeriy", "+380668887766"
print(contact_pair)

contact_pairs = [
    ("Ivan", "+380991111111"),
    ("Maxim", "+380991111112"),
    ("Olena", "+380991111113"),
]

print(contact_pairs[0][0])

for name, phone in contact_pairs:
    print("name: " + name)
    print("phone: " + phone)








