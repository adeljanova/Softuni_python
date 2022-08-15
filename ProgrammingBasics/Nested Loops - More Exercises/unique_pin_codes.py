upper_first = int(input())
upper_second = int(input())
upper_third = int(input())
pin = 0
for num1 in range(1, upper_first + 1):
    for num2 in range(1, upper_second + 1):
        for i in range(2, num2):
            if num2 % i == 0:
                break
            else:
                for num3 in range(1, upper_third + 1):
                    if num1 % 2 == 0 and num3 % 2 == 0:
                        print(f"{num1} {num2} {num3}")


