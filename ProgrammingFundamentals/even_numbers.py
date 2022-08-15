def even_numbers(numbers):
    res = 0
    for item in range(len(list_as_digits)):
        temp = int(numbers[item])
        if temp % 2 != 0:
            list_as_digits.remove(temp)
    return list_as_digits

list_of_numbers = input().split()
list_as_digits = []

for i in range(len(list_of_numbers)):
    list_as_digits.append(int(list_of_numbers[i]))
print(even_numbers(list_of_numbers))