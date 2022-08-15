budget = float(input())
category = input()
group_number = int(input())
transport = 0
ticket = 0
total_tickets_price = 0
if 1 <= group_number <= 4:
    transport = budget * 0.75
elif 5 <= group_number <= 9:
    transport = budget * 0.60
elif 10 <= group_number <= 24:
    transport = budget * 0.50
elif 25 <= group_number <= 49:
    transport = budget * 0.40
elif group_number >= 50:
    transport = budget * 0.25
money_left = budget - transport
if category == "VIP":
    ticket = 499.99
    total_tickets_price = ticket * group_number
elif category == "Normal":
    ticket = 249.99
    total_tickets_price = ticket * group_number
difference = abs(total_tickets_price - money_left)
if (transport + total_tickets_price) <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")