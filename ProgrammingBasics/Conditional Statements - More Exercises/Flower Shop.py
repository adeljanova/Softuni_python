import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())
total_price = ((magnolias * 3.25) + (hyacinths * 4) + (roses * 3.5) + (cacti * 8)) * 0.95
if total_price >= gift_price:
    money_left = total_price - gift_price
    print(f"She is left with {math.floor(money_left)} leva.")
elif total_price < gift_price:
    money_short = gift_price - total_price
    print(f"She will have to borrow {math.ceil(money_short)} leva.")



