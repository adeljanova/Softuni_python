string = input()
numbers_list = []
non_numbers_list = []
new_string = list(map(str, string))
list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol_counter = 0
for symbol in range(len(new_string)):
    if string[symbol] in list_of_numbers:
        numbers_list.append(new_string[symbol])
    else:
        non_numbers_list.append(new_string[symbol])
    symbol_counter += 1

take_list = []
skip_list = []

for num in range(len(numbers_list)):
    if num % 2 == 0:
        take_list.append(numbers_list[num])
    else:
        skip_list.append(numbers_list[num])

result_string = []

take_number = 0
skip_number = 0
while symbol_counter > 0:
    take_number = take_list[0]
    take_list.remove(take_number)
    skip_number = skip_list[0]
    skip_list.remove(skip_number)
    for i in range(0, int(take_number) + 1):
        result_string.append(non_numbers_list[i])
    for i in range(int(take_number) + 1, 0, -1):
        non_numbers_list.pop(i)
    for i in range(int(skip_number) + 1, 0, -1):
        non_numbers_list.remove(non_numbers_list[i])
    symbol_counter -= (int(take_number) + int(skip_number))
print("".join(result_string))


