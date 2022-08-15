budget = float(input())
season = input()
locations = ""
places = ""
price = 0
if budget <= 1000:
    places = "Camp"
    if season == "Summer":
        locations = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        locations = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    places = "Hut"
    if season == "Summer":
        locations = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        locations = "Morocco"
        price = budget * 0.60
else:
    places = "Hotel"
    if season == "Summer":
        locations = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        locations = "Morocco"
        price = budget * 0.90
print(f"{locations} - {places} - {price:.2f}")
