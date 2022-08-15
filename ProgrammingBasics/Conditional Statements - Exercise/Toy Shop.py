price_for_excursion = float(input())
number_of_puzzels = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_of_puzzels = number_of_puzzels * 2.60
price_of_talking_dolls = number_of_talking_dolls * 3
price_of_teddy_bears = number_of_teddy_bears * 4.10
price_of_minions = number_of_minions * 8.20
price_of_trucks = number_of_trucks * 2

total_number_of_toys = number_of_trucks + number_of_minions + number_of_puzzels + number_of_teddy_bears \
                       + number_of_talking_dolls
total_price_of_toys = price_of_puzzels + price_of_trucks + price_of_minions + price_of_teddy_bears \
                      + price_of_talking_dolls
if total_number_of_toys >= 50:
    total_price_of_toys -= total_price_of_toys * 0.25
rent = total_price_of_toys * 0.10
profit = total_price_of_toys - rent
if profit >= price_for_excursion:
    money_left = profit - price_for_excursion
    print(f"Yes! {money_left:.2f} lv left.")
elif price_for_excursion > profit:
    money_short = price_for_excursion - profit
    print(f"Not enough money! {money_short:.2f} lv needed.")
