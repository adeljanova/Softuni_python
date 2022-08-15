budget = float(input())
price_kg_flour = float(input())
price_per_pack_eggs = 0.75 * price_kg_flour
price_per_1l_milk = 1.25 * price_kg_flour
price_per_250ml_milk = price_per_1l_milk / 4
bread = price_per_250ml_milk + price_per_pack_eggs + price_kg_flour
bread_counter = 0
colored_eggs = 0
money_left = 0
while budget >= bread:
    bread_counter += 1
    budget -= bread
    colored_eggs += 3
    if bread_counter % 3 == 0:
        colored_eggs -= bread_counter - 2
    if bread > budget:
        money_left = budget
        break
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} "
      f"eggs and {money_left:.2f}BGN left.")