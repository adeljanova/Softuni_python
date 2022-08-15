budget = float(input())
command = input()
counter = 0
total_price = 0
while command != "Stop":
    counter += 1
    price_of_product = float(input())
    if counter % 3 == 0:
        price_of_product /= 2
    total_price += price_of_product
    if total_price > budget:
        print("You don't have enough money!")
        print(f"You need {total_price - budget:.2f} leva!")
        break
    command = input()
if command == "Stop":
    print(f"You bought {counter} products for {total_price:.2f} leva.")

