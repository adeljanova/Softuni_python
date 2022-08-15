from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

toys = {
    'doll': [150, 0],
    'wooden_train': [250, 0],
    'teddy_bear': [300, 0],
    'bicycle': [400, 0]
}

total_magic_level = 0
is_equal = False

while materials and magic_level:
    current_material = materials.pop()
    current_level = magic_level.popleft()
    total_magic_level = current_level * current_material

    for toy, value in toys.items():
        if total_magic_level == value[0]:
            value[1] += 1
            is_equal = True
            break
    if is_equal:
        is_equal = False
        continue

    if total_magic_level < 0:
        to_add = current_material + current_level
        materials.append(to_add)
    elif total_magic_level > 0 and not is_equal:
        materials.append(current_material + 15)
    elif current_material == 0 and current_level == 0:
        continue
    elif current_material == 0:
        magic_level.appendleft(current_level)
    elif current_level == 0:
        materials.append(current_material)


if (toys["doll"][1] > 0 and toys["wooden_train"][1] > 0) or (toys["teddy_bear"][1] > 0 and toys["bicycle"][1] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for key, value in sorted(toys.items()):
    if key == 'doll' and value[1] > 0:
        print(f"Doll: {value[1]}")
    elif key == 'wooden_train' and value[1] > 0:
        print(f"Wooden train: {value[1]}")
    elif key == 'teddy_bear' and value[1] > 0:
        print(f"Teddy bear: {value[1]}")
    elif key == 'bicycle' and value[1] > 0:
        print(f"Bicycle: {value[1]}")




