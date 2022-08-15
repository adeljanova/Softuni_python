import sys

n = int(input())
sum_numbers = 0
max_number = -sys.maxsize
for number in range(n):
    value = int(input())
    sum_numbers += value
    if value > max_number:
        max_number = value
if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum_numbers - max_number))
    print("No")
    print(f"Diff = {difference}")



