food_bought = int(input()) * 1000
command = input()
total_food = 0
while command != "Adopted":
    command = int(command)
    total_food += command
    command = input()
difference = abs(total_food - food_bought)
if total_food > food_bought:
    print(f"Food is not enough. You need {difference} grams more.")
else:
    print(f"Food is enough! Leftovers: {difference} grams.")