import math

days = int(input())
kg_food = int(input())
kg_food_for_day_dog = float(input())
kg_food_for_day_cat = float(input())
g_food_for_day_turtle = float(input())
total_food = (kg_food_for_day_cat + kg_food_for_day_dog + (g_food_for_day_turtle / 1000)) * days
if total_food <= kg_food:
    kg_left = kg_food - total_food
    print(f"{math.floor(kg_left)} kilos of food left.")
elif total_food > kg_food:
    kg_short = total_food - kg_food
    print(f"{math.ceil(kg_short)} more kilos of food are needed.")
