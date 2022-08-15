number_of_chicken_menues = int(input())
number_of_fish_menues = int(input())
number_of_vegeterian_menues = int(input())
price_for_chicken_menues = number_of_chicken_menues * 10.35
price_for_fish_menues = number_of_fish_menues * 12.40
price_for_vetererian_menues = number_of_vegeterian_menues * 8.15
dessert = (price_for_vetererian_menues + price_for_fish_menues + price_for_chicken_menues) * 20 / 100
delivery = 2.50
total_price = price_for_vetererian_menues + price_for_fish_menues + price_for_chicken_menues + delivery + dessert
print(total_price)