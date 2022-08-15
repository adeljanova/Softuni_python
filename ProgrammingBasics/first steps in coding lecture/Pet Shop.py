food_for_dogs = 2.5
food_for_cats = 4
number_of_packeges_for_dogs = int(input())
number_of_packeges_for_cats = int(input())
total_price = (number_of_packeges_for_dogs * food_for_dogs) + (number_of_packeges_for_cats * food_for_cats)
print(f"{total_price} lv.")