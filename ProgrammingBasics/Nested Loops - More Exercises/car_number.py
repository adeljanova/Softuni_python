import math


start = int(input())
finish = int(input())
for number1 in range(start, finish + 1):
    for number2 in range(start, finish + 1):
        for number3 in range(start, finish + 1):
            for number4 in range(start, finish + 1):
                if (number1 % 2 == 0 and number4 % 2 != 0) or (number1 % 2 != 0 and number4 % 2 == 0):
                    if number1 > number4:
                        if (number2 + number3) % 2 == 0:
                            print(str(number1) + str(number2) + str(number3) + str(number4), end=" ")