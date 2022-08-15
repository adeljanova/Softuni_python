month = input()
nights = int(input())
studio = 0
apartment = 0
price_studio = 0
price_apartment = 0
if month in "May October":
    studio = 50
    apartment = 65
    price_studio = studio * nights
    price_apartment = apartment * nights
    if 7 < nights <= 14 and studio:
        price_studio = studio * nights * 0.95
    elif nights > 14 and studio:
        price_studio = studio * nights * 0.70
    if nights > 14 and apartment:
        price_apartment = apartment * nights * 0.90
elif month in "June September":
    studio = 75.20
    apartment = 68.70
    price_studio = studio * nights
    price_apartment = apartment * nights
    if nights > 14 and studio:
        price_studio = studio * nights * 0.80
    if nights > 14 and apartment:
        price_apartment = apartment * nights * 0.90
elif month in "July August":
    studio = 76
    apartment = 77
    price_studio = studio * nights
    price_apartment = apartment * nights
    if nights > 14 and apartment:
        price_apartment = apartment * nights * 0.90

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

