from collections import deque


def taking_normal_boxes(curr_elf, curr_box, energy_taken, toys, bool):

    if curr_elf >= curr_box:
        energy_taken += curr_box
        curr_elf -= curr_box
        curr_elf += 1
        toys += 1
        bool = True
    else:
        curr_elf *= 2

    return curr_elf, curr_box, energy_taken, toys, bool


def taking_ox_for_third_time(curr_elf, curr_box, energy_taken, toys, bool):

    if curr_elf >= curr_box * 2:
        energy_taken += curr_box * 2
        curr_elf -= (curr_box * 2)
        curr_elf += 1
        toys += 2
        bool = True
    else:
        curr_elf *= 2

    return curr_elf, curr_box, energy_taken, toys, bool


def taking_box_for_fifth_time(curr_elf, curr_box, energy_taken, toys, bool):

    if curr_elf >= curr_box:
        curr_elf -= curr_box
        energy_taken += curr_box
        bool = True
    else:
        curr_elf *= 2

    return curr_elf, curr_box, energy_taken, toys, bool


def taking_box_when_third_and_fifth_time_equals(curr_elf, curr_box, energy_taken, toys, bool):

    if curr_elf >= curr_box * 2:
        energy_taken += curr_box * 2
        curr_elf -= (curr_box * 2)
        bool = True
    elif curr_elf >= curr_box:
        energy_taken += curr_box
        curr_elf -= curr_box
        bool = True
    else:
        curr_elf *= 2

    return curr_elf, curr_box, energy_taken, toys, bool


elfs_energy = deque(map(int, input().split()))
num_materials_in_box = deque(map(int, input().split()))

santa_bag = 0
counter = 0
total_energy = 0

while num_materials_in_box and elfs_energy:
    is_happened = False
    current_elf = elfs_energy.popleft()

    counter += 1
    if current_elf < 5:
        continue

    current_box = num_materials_in_box.pop()
    if counter % 3 != 0 and counter % 5 != 0:
        current_elf, current_box, total_energy, santa_bag, is_happened =\
            taking_normal_boxes(current_elf, current_box, total_energy, santa_bag, is_happened)

    elif counter % 3 == 0 and counter % 5 == 0:
        current_elf, current_box, total_energy, santa_bag, is_happened =\
            taking_box_when_third_and_fifth_time_equals(current_elf, current_box, total_energy, santa_bag, is_happened)

    elif counter % 3 == 0:
        current_elf, current_box, total_energy, santa_bag, is_happened =\
            taking_ox_for_third_time(current_elf, current_box, total_energy, santa_bag, is_happened)

    elif counter % 5 == 0:
        current_elf, current_box, total_energy, santa_bag, is_happened =\
            taking_box_for_fifth_time(current_elf, current_box, total_energy, santa_bag, is_happened)

    if not is_happened:
        num_materials_in_box.append(current_box)
    elfs_energy.append(current_elf)


print(f"Toys: {santa_bag}")
print(f"Energy: {total_energy}")
if elfs_energy:
    print(f'Elves left: {", ".join(str(x) for x in elfs_energy)}')
if num_materials_in_box:
    print(f'Boxes left: {", ".join(str(x) for x in num_materials_in_box)}')






