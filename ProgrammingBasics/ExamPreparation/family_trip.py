budget = float(input())
num_nights = int(input())
price_for_night = float(input())
percent_extra_spendings = int(input())
if num_nights > 7:
    price_for_night -= price_for_night * 0.05
total_price = num_nights * price_for_night
extra_spendings = budget * (percent_extra_spendings / 100)
total_price += extra_spendings
difference = abs(budget - total_price)
if total_price <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")