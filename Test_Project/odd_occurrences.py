from collections import Counter

words_list = input().split()

new_list = []
for word in words_list:
    new_list.append(word.lower())

course_dict = Counter(new_list)

output = []
for key, value in course_dict.items():
    if value % 2 != 0:
        output.append(key)

print(" ".join(output))


