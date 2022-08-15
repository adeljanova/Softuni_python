rows, columns = [int(x) for x in input().split()]

alphabet = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z'
}
matrix = []

for row in range(rows):
    palindrome = []
    if row in alphabet.keys():
        palindrome.append(alphabet[row])
    for col in range(columns):
        temp = row + col
        if temp in alphabet.keys():
            palindrome.append(alphabet[temp])
        palindrome.append(alphabet[row])
        matrix.append(palindrome)
        palindrome = [alphabet[row]]
counter = 0
for row in matrix:
    print(*row, sep="", end=' ')
    counter += 1
    if counter == columns:
        print()
        counter = 0



