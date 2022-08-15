list_of_numbers = list(map(int, input().split(", ")))

max_num = str(max(list_of_numbers))
groups = (int(max_num) // 10)
if int(max_num) % 10 != 0:
    groups += 1
new_list = []
for group in range(1, groups + 1):
    group_number = int(str(group) + str(0))
    for number in list_of_numbers:
        if (group_number - 10) < number <= group_number:
            new_list.append(number)
    print(f"Group of {group_number}'s: {new_list}")
    new_list = []


