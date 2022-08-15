num_days = int(input())
total_food = float(input())
total_food_dog = 0
total_food_cat = 0
biscuits = 0
for day in range(1, num_days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_food_dog += dog_food
    total_food_cat += cat_food
    if day % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1
total_food_eaten = (total_food_dog + total_food_cat) / total_food * 100
food_eaten_from_dog = total_food_dog / (total_food_dog + total_food_cat) * 100
food_eaten_from_cat = total_food_cat / (total_food_dog + total_food_cat) * 100
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_eaten:.2f}% of the food has been eaten.")
print(f"{food_eaten_from_dog:.2f}% eaten from the dog.")
print(f"{food_eaten_from_cat:.2f}% eaten from the cat.")
