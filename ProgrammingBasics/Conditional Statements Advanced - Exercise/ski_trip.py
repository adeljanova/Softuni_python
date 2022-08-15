days = int(input())
type_of_room = input()
grade = input()
nights = days - 1
total_price = 0
if type_of_room == "room for one person":
    total_price = nights * 18.00
elif type_of_room == "apartment":
    total_price = nights * 25.00
    if days < 10:
        total_price -= total_price * 0.30
    elif 10 <= days < 15:
        total_price -= total_price * 0.35
    elif days >= 15:
        total_price -= total_price * 0.50
elif type_of_room == "president apartment":
    total_price = nights * 35.00
    if days < 10:
        total_price -= total_price * 0.10
    elif 10 <= days < 15:
        total_price -= total_price * 0.15
    elif days >= 15:
        total_price -= total_price * 0.20

if grade == "positive":
    total_price += total_price * 0.25
elif grade == "negative":
    total_price -= total_price * 0.10
print(f"{total_price:.2f}")