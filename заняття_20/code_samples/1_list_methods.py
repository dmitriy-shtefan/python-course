topics = ["списки", "словники", "множини", "списки"]

topics.append("кортежі")
topics.remove("словники")

print(topics)
print(topics.count("списки"))
print(topics.index("множини"))
print("кортежі" in topics)
