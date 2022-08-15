budget = float(input())
season = input()
destination = 0
rest = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        rest = "Camp"
        budget -= budget * 0.70
    elif season == "winter":
        rest = "Hotel"
        budget -= budget * 0.30
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        rest = "Camp"
        budget -= budget * 0.60
    elif season == "winter":
        rest = "Hotel"
        budget -= budget * 0.20
else:
    destination = "Europe"
    if season in "summer winter":
        rest = "Hotel"
        budget -= budget * 0.10

print(f"Somewhere in {destination}")
print(f"{rest} - {budget:.2f}")



