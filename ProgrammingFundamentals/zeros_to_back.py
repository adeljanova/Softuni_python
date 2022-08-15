string = input().split(", ")
index_number = -1
counter = 0
zeros_iteration = 0
string_as_digits = []
for number in string:
    string_as_digits.append(int(number))
    if int(number) == 0:
        counter += 1
for i in range(0, len(string_as_digits)):
    index_number += 1
for index in range(0, len(string_as_digits)):
    if string_as_digits[index] == 0:
        if string_as_digits[index_number] == 0:
            continue
        else:
            string_as_digits[index], string_as_digits[index_number] =\
                string_as_digits[index_number], string_as_digits[index]
            index_number -= 1
            zeros_iteration += 1
        if zeros_iteration == counter:
            break
print(string_as_digits)

