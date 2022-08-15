text = input()
reverse_word = ""
for i in range(len(text) - 1, -1, -1):
    reverse_word += text[i]
print(reverse_word)
