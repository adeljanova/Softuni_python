word = input()

reversed_word = ""

while word != "end":
    for ch in reversed(word):
        reversed_word += ch
    print(f"{word} = {reversed_word}")
    reversed_word = ""
    word = input()