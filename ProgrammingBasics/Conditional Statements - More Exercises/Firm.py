import math

needed_hours = int(input())
days_firm_have = int(input())
workers_working_overtime = int(input())
training_days = days_firm_have * 0.10
total_time = math.floor((days_firm_have - training_days) * 8 + (workers_working_overtime * 2 * days_firm_have))
if total_time >= needed_hours:
    hours_left = total_time - needed_hours
    print(f"Yes!{hours_left} hours left.")
elif total_time < needed_hours:
    hours_short = needed_hours - total_time
    print(f"Not enough time!{hours_short} hours needed.")