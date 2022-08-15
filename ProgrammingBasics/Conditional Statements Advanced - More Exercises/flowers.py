chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
if_holiday = input()
price_chrysanthemums = 0
price_roses = 0
price_tulips = 0
if season in "Spring Summer":
    price_chrysanthemums = chrysanthemums * 2
    price_roses = roses * 4.10
    price_tulips = tulips * 2.50
elif season in "Autumn Winter":
    price_chrysanthemums = chrysanthemums * 3.75
    price_roses = roses * 4.50
    price_tulips = tulips * 4.15
total_flowers = chrysanthemums + roses + tulips
total_price = price_tulips + price_roses + price_chrysanthemums
if if_holiday == "Y":
    total_price += total_price * 0.15
if tulips > 7 and season == "Spring":
    total_price -= total_price * 0.05
elif roses >= 10 and season == "Winter":
    total_price -= total_price * 0.10
if total_flowers > 20 and season in "Spring Summer Autumn Winter":
    total_price -= total_price * 0.20
total_price_plus_bucket = total_price + 2
print(f"{total_price_plus_bucket:.2f}")
