minutes_per_day = int(input())
num_of_walks = int(input())
calories = int(input())
burned_calories = minutes_per_day * num_of_walks * 5
if burned_calories >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")