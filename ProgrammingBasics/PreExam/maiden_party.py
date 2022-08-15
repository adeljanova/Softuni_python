price_for_party = float(input())
num_lover_letters = int(input())
num_roses = int(input())
num_keychains = int(input())
num_cartoons = int(input())
num_lucky_surprices = int(input())
total_buyings = num_cartoons + num_keychains + num_roses + num_lucky_surprices + num_lover_letters
total_price = num_cartoons * 18.20 + num_keychains * 3.60 + num_roses * 7.20 + num_lucky_surprices * 22 \
              + num_lover_letters * 0.60
if total_buyings > 25:
    total_price -= total_price * 0.35
hosting = total_price * 0.1
total_price -= hosting
difference = abs(total_price - price_for_party)
if total_price >= price_for_party:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")