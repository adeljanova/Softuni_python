def factorial(num1, num2):
    res1 = 1
    res2 = 1
    result = 0
    for num in range(1, num1 + 1):
        res1 *= num
    for num in range(1, num2 + 1):
        res2 *= num
    result = res1 / res2
    return f"{result:.2f}"


number_one = int(input())
number_two = int(input())
print(factorial(number_one, number_two))