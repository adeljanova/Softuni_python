goal_for_the_day = int(input())
command = input()
price = 0
total_price = 0
while command != "closed":
    if command == "haircut":
        type_haircut = input()
        if type_haircut == "mens":
            price = 15
        elif type_haircut == "ladies":
            price = 20
        elif type_haircut == "kids":
            price = 10
    elif command == "color":
        type_color = input()
        if type_color == "touch up":
            price = 20
        elif type_color == "full color":
            price = 30
    total_price += price
    if total_price >= goal_for_the_day:
        break
    command = input()
if total_price >= goal_for_the_day:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {abs(total_price - goal_for_the_day)}lv. more.")
print(f"Earned money: {total_price}lv.")
