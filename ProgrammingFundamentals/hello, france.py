items_with_their_prices = input().split("|")
budget = float(input())
train_ticket = 150
profit = 0
new_list = []
temp_budget = budget
single_profit = 0
for item in items_with_their_prices:
    temp_items_with_their_prices = item.split("->")
    temp_type = temp_items_with_their_prices[0]
    temp_price = float(temp_items_with_their_prices[1])
    if "Clothes" in temp_items_with_their_prices:
        if temp_price <= 50:
            if temp_budget >= temp_price:
                temp_budget -= temp_price
                single_profit = temp_price * 1.4
                profit += single_profit
                new_list.append(f"{single_profit:.2f}")
    elif "Shoes" in temp_items_with_their_prices:
        if temp_price <= 35:
            if temp_budget >= temp_price:
                temp_budget -= temp_price
                single_profit = temp_price * 1.4
                profit += single_profit
                new_list.append(f"{single_profit:.2f}")
    elif "Accessories" in temp_items_with_their_prices:
        if temp_price <= 20.50:
            if temp_budget >= temp_price:
                temp_budget -= temp_price
                single_profit = temp_price * 1.4
                profit += single_profit
                new_list.append(f"{single_profit:.2f}")
print(*new_list, sep=" ")
print(f"Profit: {(temp_budget + profit) - budget:.2f}")
if temp_budget + profit >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")