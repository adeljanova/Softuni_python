from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words_to_find = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}

is_word_found = False
while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key, value in words_to_find.items():
        if current_vowel in key:
            words_to_find[key] = words_to_find[key].replace(current_vowel, "")
        if current_consonant in key:
            words_to_find[key] = words_to_find[key].replace(current_consonant, "")

        if words_to_find[key] == "":
            print(f"Word found: {key}")
            is_word_found = True
            break
    if is_word_found:
        break

if not is_word_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join([x for x in vowels])}")
if consonants:
    print(f"Consonants left: {' '.join([x for x in consonants])}")