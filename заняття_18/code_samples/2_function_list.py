## Функція, список і умова

def count_long_words(words):
    count = 0

    for word in words:
        if len(word) > 5:
            count += 1

    return count


languages = ["Python", "Java", "Scratch", "C++"]
result = count_long_words(languages)

print(result)
print(languages[1])
