day_of_week = input()
ticket = 0
if day_of_week in "Monday Tuesday Friday ":
    ticket = 12
elif day_of_week in "Wednesday Thursday":
    ticket = 14
elif day_of_week in "Saturday Sunday":
    ticket = 16
print(ticket)