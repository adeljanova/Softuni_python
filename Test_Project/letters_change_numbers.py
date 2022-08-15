data = input().split()

result = 0
number = ''
letters = ''

for word in data:
    for ch in range(len(word)):
        if word[ch].isdigit():
            number += word[ch]
        else:
            letters += word[ch]
    number = int(number)
    switch = 0
    for ch in letters:
        if switch == 0:
            if ch.isupper():
                number /= (ord(ch) - 64)
            elif ch.islower():
                number *= (ord(ch) - 96)
        else:
            if ch.isupper():
                number -= (ord(ch) - 64)
            elif ch.islower():
                number += (ord(ch) - 96)
        switch += 1
    result += number
    number = ''
    letters = ''

print(f"{result:.2f}")


