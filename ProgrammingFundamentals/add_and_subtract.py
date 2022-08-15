def sum_numbers(num1, num2):
    result = num1 + num2
    return result

def subtract(result, num3):
    end_result = result - num3
    return end_result

num_one = int(input())
num_two = int(input())
num_three = int(input())

print(subtract(sum_numbers(num_one, num_two), num_three))
