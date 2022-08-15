list_of_numbers = input().split()
list_of_numbers_as_digits = []
total = 0
average = 0
counter_num_in_list = 0
tops_counter = 0
new_list = []
isValid = True
for string in range(len(list_of_numbers)):
    list_of_numbers_as_digits.append(int(list_of_numbers[string]))
    total += int(list_of_numbers[string])
    counter_num_in_list += 1
average = total / counter_num_in_list

for number in range(len(list_of_numbers_as_digits) - 1, -1, -1):
    temp_number = list_of_numbers_as_digits[number]
    if temp_number > average:
        tops_counter += 1
        new_list.append(temp_number)
    else:
        continue
    if tops_counter >= 5:
        break
if len(new_list) == 0:
    print("No")
else:
    new_list.sort(reverse=True)
    print(*new_list)
