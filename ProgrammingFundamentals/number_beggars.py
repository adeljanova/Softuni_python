string_of_integers = input().split(", ")
count_of_beggars = int(input())
temp_sum = 0
new_list = []
counter_index = 0
for beggar in range(1, count_of_beggars + 1):
    for index in range(counter_index, len(string_of_integers), count_of_beggars):
        temp_sum += int(string_of_integers[index])
    new_list.append(temp_sum)
    temp_sum = 0
    counter_index += 1
print(new_list)