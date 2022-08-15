start = input()
finish = input()
excluded = input()
counter = 0
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
keywords = []
for letter1 in alphabets:
    for letter2 in alphabets:
        for letter3 in alphabets:
            keywords.append(letter1 + letter2 + letter3)
