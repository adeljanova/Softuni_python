n = int(input())
list_of_numbers = []
new_list = []
for numbers in range(0, n):
    number = int(input())
    list_of_numbers.append(number)
command = input()
for num in range(len(list_of_numbers)):
    temp_number = list_of_numbers[num]
    if command == "even":
        if temp_number % 2 == 0:
            new_list.append(temp_number)
    elif command == "odd":
        if temp_number % 2 != 0:
            new_list.append(temp_number)
    elif command == "positive":
        if temp_number >= 0:
            new_list.append(temp_number)
    elif command == "negative":
        if temp_number < 0:
            new_list.append(temp_number)
print(new_list)
