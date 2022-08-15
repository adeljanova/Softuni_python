import sys


def smallest_number(num1, num2, num3):
    temp = min(num1, num2, num3)
    return temp

num_one = int(input())
num_two = int(input())
num_three = int(input())

print(smallest_number(num_one, num_two, num_three))