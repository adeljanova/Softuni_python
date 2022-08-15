excursion_money = float(input())
balance = float(input())
past_days = 0
spending_counter = 0
while balance < excursion_money and spending_counter < 5:
    spend_or_save = input()
    money_save_spend = float(input())
    past_days += 1
    if spend_or_save == "save":
        balance += money_save_spend
        spending_counter = 0

    elif spend_or_save == "spend":
        balance -= money_save_spend
        spending_counter += 1
        if balance < 0:
            balance = 0
if spending_counter == 5:
    print(f"You can't save the money.")
    print(f"{past_days}")

elif balance >= excursion_money:
    print(f"You saved the money for {past_days} days.")

