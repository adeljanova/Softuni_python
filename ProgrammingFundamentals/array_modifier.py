numbers_array = input().split()
command = input()
numbers_array_as_digits = []
for num in range(len(numbers_array)):
    numbers_array_as_digits.append(int(numbers_array[num]))
while command != "end":
    if "decrease" in command:
        for element in range(len(numbers_array_as_digits)):
            numbers_array_as_digits[element] -= 1
    else:
        command = command.split()
        index_one = int(command[1])
        index_two = int(command[2])
        if "swap" in command:
            numbers_array_as_digits[index_one], numbers_array_as_digits[index_two] =\
                numbers_array_as_digits[index_two], numbers_array_as_digits[index_one]
        elif "multiply" in command:
            temp_one = numbers_array_as_digits[index_one]
            temp_two = numbers_array_as_digits[index_two]
            result = temp_one * temp_two
            numbers_array_as_digits[index_one] = result
    command = input()
print(*numbers_array_as_digits, sep=", ")