bottles = int(input())
quantity_bottles = bottles * 750
washings = input()
total_dishes = 0
quantity_dishes_pots = 0
total_pots = 0
days = 0
new_washings = 0
while washings != "End":
    washings = int(washings)
    days += 1
    if days % 3 == 0:
        quantity_dishes_pots = washings * 15
        total_pots += washings

    else:
        quantity_dishes_pots = washings * 5
        total_dishes += washings

    quantity_bottles -= quantity_dishes_pots
    if quantity_bottles < 0:
        print(f"Not enough detergent, {abs(quantity_bottles)} ml. more necessary!")
        break
    washings = input()

if washings == "End" and quantity_bottles >= 0:
    print(f"Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {quantity_bottles} ml.")


