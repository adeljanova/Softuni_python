list_of_numbers = input().split()
n = int(input())
temp_list = []
temp = 0
counter = 0
for index in range(len(list_of_numbers)):
    temp_list.append(int(list_of_numbers[index]))
for iteration in range(0, n):
    temp_number = min(temp_list)
    temp_list.remove(temp_number)
print(*temp_list, sep=", ")




