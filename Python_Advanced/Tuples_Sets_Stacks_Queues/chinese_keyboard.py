sequence_of_words = input().split(", ")

top_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
middle_row = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
bottom_row = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

is_top = True
is_middle = True
is_bottom = True

output = []
for word in sequence_of_words:
    for letter in word:
        if letter not in top_row:
            is_top = False
            break
    for letter in word:
        if letter not in middle_row:
            is_middle = False
            break
    for letter in word:
        if letter not in bottom_row:
            is_bottom = False
            break
    if is_top:
        output.append(word)
    if is_middle:
        output.append(word)
    if is_bottom:
        output.append(word)
    is_top = True
    is_middle = True
    is_bottom = True
print(', '.join(output))
