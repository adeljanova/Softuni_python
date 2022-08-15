age = int(input())
laundry_price = float(input())
toy_price = int(input())
birthday_money = 0
toys = 0
total_money_price = 0
for years in range(1, age + 1):
    if years % 2 != 0:
        toys += 1
    else:
        birthday_money += 10
        total_money_price += birthday_money - 1
total_toys_price = toy_price * toys
total_price = total_money_price + total_toys_price
difference = abs(total_price - laundry_price)
if total_price >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")