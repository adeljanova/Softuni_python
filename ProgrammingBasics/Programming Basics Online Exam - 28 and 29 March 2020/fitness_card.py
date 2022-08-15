sum = float(input())
sex = input()
age = int(input())
sport = input()
total = 0
if sport == "Gym":
    if sex == "m":
        total = 42
    elif sex == "f":
        total = 35
elif sport == "Boxing":
    if sex == "m":
        total = 41
    elif sex == "f":
        total = 37
elif sport == "Yoga":
    if sex == "m":
        total = 45
    elif sex == "f":
        total = 42
elif sport == "Zumba":
    if sex == "m":
        total = 34
    elif sex == "f":
        total = 31
elif sport == "Dances":
    if sex == "m":
        total = 51
    elif sex == "f":
        total = 53
elif sport == "Pilates":
    if sex == "m":
        total = 39
    elif sex == "f":
        total = 37
if age < 20:
    total = total * 0.8
if total <= sum:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(sum - total):.2f} more.")