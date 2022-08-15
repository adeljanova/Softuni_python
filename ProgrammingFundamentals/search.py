n = int(input())
word = input()
all_word_list = []
for phrases in range(0, n):
    phrase = input()
    all_word_list.append(phrase)
print(all_word_list)
for words in range(len(all_word_list) - 1, -1, -1):
    element = all_word_list[words]
    if word not in element:
        all_word_list.remove(element)
print(all_word_list)
