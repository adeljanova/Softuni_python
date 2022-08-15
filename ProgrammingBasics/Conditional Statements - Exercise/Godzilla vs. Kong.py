buget_for_the_film = float(input())
number_of_extra = int(input())
price_for_clothes_for_one_extra = float(input())
decor = buget_for_the_film * 0.10
total_price_for_clothes = price_for_clothes_for_one_extra * number_of_extra
if number_of_extra > 150:
    total_price_for_clothes -= total_price_for_clothes * 0.10
if decor + total_price_for_clothes > buget_for_the_film:
    money_short = (decor + total_price_for_clothes) - buget_for_the_film
    print(f"Not enough money!")
    print(f"Wingard needs {money_short:.2f} leva more.")
elif decor + total_price_for_clothes <= buget_for_the_film:
    money_left = buget_for_the_film - (decor + total_price_for_clothes)
    print(f"Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")