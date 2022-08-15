inheritance = float(input())
year_must_live = int(input())
spendings = 0
money_left = 0
start_age = 17
for year in range(1800, year_must_live + 1):
    start_age += 1
    if year % 2 == 0:
        spendings += 12000

    else:
        spendings += 12000 + 50 * start_age
money_left = abs(inheritance - spendings)
if inheritance >= spendings:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {money_left:.2f} dollars to survive." )