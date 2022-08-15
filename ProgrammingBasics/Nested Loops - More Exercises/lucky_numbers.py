import math


N = int(input())
for number in range(1000, 10000):
    dublicate = number
    while dublicate > 0:
        fourth_dig = math.ceil(dublicate % 10)
        dublicate = math.ceil(dublicate // 10)
        third_dig = math.ceil(dublicate % 10)
        dublicate = math.ceil(dublicate // 10)
        second_dig = math.ceil(dublicate % 10)
        dublicate = math.ceil(dublicate // 10)
        first_dig = math.ceil(dublicate % 10)
        dublicate = 0
        if first_dig != 0 and second_dig != 0 and third_dig != 0 and fourth_dig != 0:
            if first_dig + second_dig == third_dig + fourth_dig:
                if N % (first_dig + second_dig) == 0:
                    print(number, end=" ")
