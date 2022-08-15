data = input().split(", ")

for word in data:
    if 2 < len(word) < 17:
        if word.isalnum() or "-" in word or "_" in word:
            print(word)

