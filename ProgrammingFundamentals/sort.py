def sort(numbers):
    numbers = sorted(numbers)
    return numbers

list_of_numbers = input().split()
list_as_digits = []
for i in range(len(list_of_numbers)):
    list_as_digits.append(int(list_of_numbers[i]))
print(sort(list_as_digits))