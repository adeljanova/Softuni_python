def min_of_numbers(numbers):
    return f"The minimum number is {min(numbers)}"

def max_of_numbers(numbers):
    return f"The maximum number is {max(numbers)}"

def sum_of_numbers(numbers):
    sum = 0
    for num in range(len(list_as_digits)):
        sum += int(list_as_digits[num])
    return f"The sum number is: {sum}"

list_of_numbers = input().split()
list_as_digits = []
for i in range(len(list_of_numbers)):
    list_as_digits.append(int(list_of_numbers[i]))

print(min_of_numbers(list_as_digits))
print(max_of_numbers(list_as_digits))
print(sum_of_numbers(list_as_digits))

