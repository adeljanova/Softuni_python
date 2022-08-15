string = input()

digits = ''
letters = ''
symbols = ''
for symbol in string:
    if 47 < ord(symbol) < 58:
        digits += symbol
    elif 64 < ord(symbol) < 91 or 96 < ord(symbol) < 123:
        letters += symbol
    else:
        symbols += symbol
print(digits)
print(letters)
print(symbols)