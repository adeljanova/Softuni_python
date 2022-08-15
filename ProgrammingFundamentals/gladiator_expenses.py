lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expences = 0
counter = 0
for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        expences += helmet_price
    if i % 3 == 0:
        expences += sword_price
        if i % 2 == 0:
            expences += shield_price
            counter += 1
            if counter % 2 == 0:
                expences += armor_price
print(f"Gladiator expenses: {expences:.2f} aureus")

