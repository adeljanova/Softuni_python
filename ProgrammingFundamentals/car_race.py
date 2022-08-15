list_of_numbers = input().split()
left_player_time = 0
right_player_time = 0
position_counter = 0
list_of_numbers_as_digits = []
for number in range(len(list_of_numbers)):
    list_of_numbers_as_digits.append(int(list_of_numbers[number]))
for position_left in range(0, len(list_of_numbers_as_digits)):
    if list_of_numbers_as_digits[position_left] == 0:
        left_player_time *= 0.8
    else:
        left_player_time += list_of_numbers_as_digits[position_left]
    position_counter += 1
    if position_counter == len(list_of_numbers_as_digits) // 2:
        break
position_counter = 0
for position_right in range(len(list_of_numbers_as_digits) - 1, -1, -1):
    if list_of_numbers_as_digits[position_right] == 0:
        right_player_time *= 0.8
    else:
        right_player_time += list_of_numbers_as_digits[position_right]
    position_counter += 1
    if position_counter == len(list_of_numbers_as_digits) // 2:
        break
if right_player_time > left_player_time:
    print(f"The winner is left with total time: {left_player_time:.1f}")
else:
    print(f"The winner is right with total time: {right_player_time:.1f}")
