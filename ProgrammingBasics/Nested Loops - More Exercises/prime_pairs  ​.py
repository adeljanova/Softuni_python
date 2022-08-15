start_first_couple = int(input())
start_second_couple = int(input())
difference_first_couple = int(input())
difference_second_couple = int(input())
flag = False
first = start_first_couple
second = start_second_couple
for first in range(start_first_couple, start_first_couple + difference_first_couple + 1):
    for second in range(start_second_couple, start_second_couple + difference_second_couple + 1):
        for i in range(2, int(first / 2) + 1):
            if first % i == 0:
                flag = True
                break
            else:
                print(first, end=" ")
        for i in range(2, int(second / 2) + 1):
            if second % i == 0:
                flag = True
                break
            else:
                print(second, end=" ")



#     for i in range(2, int(first / 2) + 1):
#         if first % i == 0:
#             flag = True
#             break
#     print(first)
#     for i in range(2, int(second / 2) + 1):
#         if second % i == 0:
#             flag = True
#             break
#     print(second)
# print(str(first) + str(second))