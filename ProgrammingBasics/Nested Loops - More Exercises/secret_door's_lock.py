import math


upper_hundreds = int(input())
upper_tens = int(input())
upper_units = int(input())

for hundred in range(1, upper_hundreds + 1):
    for ten in range(1, upper_tens + 1):
        for unit in range(1, upper_units + 1):
            if hundred % 2 == 0 and unit % 2 == 0:
                for i in range(2, int(math.sqrt(ten)) + 1):
                    if ten % i != 0:
                        print(hundred, ten, unit)
                        break
