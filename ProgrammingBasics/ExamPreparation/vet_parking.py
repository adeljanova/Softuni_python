days = int(input())
hours = int(input())
counter_days = 0
counter_hours = 0
tax = 0
total_tax = 0

for d in range(1, days + 1):
    counter_days += 1
    daily_tax = 0
    counter_hours = 0
    for h in range(1, hours + 1):

        counter_hours += 1
        if counter_days % 2 == 0 and counter_hours % 2 != 0:
            tax = 2.50
        elif counter_days % 2 != 0 and counter_hours % 2 == 0:
            tax = 1.25
        else:
            tax = 1
        daily_tax += tax
    total_tax += daily_tax
    print(f"Day: {counter_days} - {daily_tax:.2f} leva")
print(f"Total: {total_tax:.2f} leva")
