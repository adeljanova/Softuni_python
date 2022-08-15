list_of_numbers = input().split()

new_list = []
for item in range(len(list_of_numbers)):
    new_list.append(abs(float(list_of_numbers[item])))
print(new_list)
