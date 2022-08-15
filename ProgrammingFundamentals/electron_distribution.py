num_of_electrons = int(input())

shells_list = []
position_counter = 1
while num_of_electrons > 0:
    max_num = 2 * (position_counter ** 2)
    if num_of_electrons < max_num:
        shells_list.append(num_of_electrons)
    else:
        shells_list.append(max_num)
    num_of_electrons -= max_num
    position_counter += 1

print(shells_list)