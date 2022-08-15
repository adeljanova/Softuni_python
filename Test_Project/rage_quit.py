import re

data = input()

data = data.upper()
unique_symbols = 0
list_unique = ''
collecter = ''
data_list = []
for symbol in data:
    if symbol not in list_unique:
        if symbol.islower() or symbol.isupper() or (not symbol.isalnum()):
            unique_symbols += 1
            list_unique += symbol
print(f"Unique symbols used: {unique_symbols}")
split_data = re.split('(\d+)',data)
split_data.remove(split_data[-1])

for i in range(0, len(split_data), 2):
    collecter += (split_data[i] * (int(split_data[i + 1])))
print(collecter)



