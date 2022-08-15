def is_palindrome(numbers):
    for number in range(len(list_as_digits)):
        is_valid = False
        reversed = 0
        temp_number = list_as_digits[number]
        while temp_number > 0:
            temp_digit = temp_number % 10
            reversed = reversed * 10 + temp_digit
            temp_number //= 10
        if list_as_digits[number] == reversed:
            is_valid = True
        if is_valid:
            print("True")
        else:
            print("False")

list_of_numbers = input().split(", ")
list_as_digits = []
for i in range(len(list_of_numbers)):
    list_as_digits.append(int(list_of_numbers[i]))

is_palindrome(list_as_digits)
