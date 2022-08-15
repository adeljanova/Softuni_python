import math

square_feet_vineyard = int(input())
grapes_for_one_square_feet = float(input())
needed_wine_litres = int(input())
number_of_workers = int(input())
total_grapes = square_feet_vineyard * grapes_for_one_square_feet
harvest_for_wine = total_grapes * 0.40
litres_of_wine = harvest_for_wine / 2.5
if litres_of_wine < needed_wine_litres:
    wine_short = needed_wine_litres - litres_of_wine
    print(f"It will be a tough winter! More {math.floor(wine_short)} liters wine needed.")
elif litres_of_wine >= needed_wine_litres:
    print(f"Good harvest this year! Total wine: {math.floor(litres_of_wine)} liters.")
    wine_left = litres_of_wine - needed_wine_litres
    wine_for_one_worker = wine_left / number_of_workers
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_for_one_worker)} liters per person.")

