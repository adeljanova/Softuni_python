peters_budget = float(input())
number_of_videocards = int(input())
number_of_procesors = int(input())
number_of_ram = int(input())

price_for_videocards = number_of_videocards * 250
price_for_one_procesor = price_for_videocards * 0.35
total_price_for_procesors = number_of_procesors * price_for_one_procesor
price_for_one_ram = price_for_videocards * 0.10
total_price_for_ram = number_of_ram * price_for_one_ram
total_price = price_for_videocards + total_price_for_ram + total_price_for_procesors

if number_of_videocards > number_of_procesors:
     total_price -= total_price * 0.15
if peters_budget >= total_price:
    money_left = peters_budget - total_price
    print(f"You have {money_left:.2f} leva left!")
elif peters_budget < total_price:
    money_needed = total_price - peters_budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")
