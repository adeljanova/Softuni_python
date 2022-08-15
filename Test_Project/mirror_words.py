import re

text = input()
pattern = r"(?P<symbols>(@|#))(?P<word_1>[A-Za-z]{3,})(?P=symbols)(?P=symbols)(?P<word_2>[A-Za-z]{3,})(?P=symbols)"
matches = re.finditer(pattern, text)

palindrome = []
counter = 0
for match in matches:
    current = match.groupdict()
    if current["word_1"] == current["word_2"][::-1]:
        palindrome.append(current["word_1"])
    counter += 1

if counter == 0:
    print("No word pairs found!")
else:
    print(f"{counter} word pairs found!")
if not palindrome:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(f"{word} <=> {word[::-1]}" for word in palindrome))

