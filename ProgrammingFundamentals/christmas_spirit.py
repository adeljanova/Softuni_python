quantity = int(input())
days = int(input())
spirit = 0
total_money = 0
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_money += ornament_set * quantity
        spirit += 5
    if day % 3 == 0:
        total_money += (tree_skirt + tree_garlands) * quantity
        spirit += 13
    if day % 5 == 0:
        total_money += tree_lights * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        total_money += (tree_skirt + tree_garlands + tree_lights)
        spirit -= 20

if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {total_money}")
print(f"Total spirit: {spirit}")