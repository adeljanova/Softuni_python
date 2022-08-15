people = int(input())
season = input()
price_per_person = 0
if people < 6:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.50
    elif season == "autumn":
        price_per_person = 60
    elif season == "winter":
        price_per_person = 86
else:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.50
    elif season == "winter":
        price_per_person = 85
total_price = price_per_person * people
if season == "summer":
    total_price -= total_price * 0.15
elif season == "winter":
    total_price += total_price * 0.08
print(f"{total_price:.2f} leva.")