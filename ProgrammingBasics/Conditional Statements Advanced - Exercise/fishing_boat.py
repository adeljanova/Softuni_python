budget = int(input())
season = input()
fishers = int(input())
rent = 0

if season == "Spring":
    rent = 3000
elif season in "Summer Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishers <= 6:
    rent -= rent * 0.10
elif 7 < fishers <= 11:
    rent -= rent * 0.15
elif fishers >= 12:
    rent -= rent * 0.25

if fishers % 2 == 0 and season in "Spring Summer Winter":
    rent -= rent * 0.05

left_money = abs(budget - rent)
if budget >= rent:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")