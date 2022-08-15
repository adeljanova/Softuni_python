import math
name_of_series = input()
duration_of_episode = int(input())
duration_of_break = int(input())
time_for_lunch = duration_of_break * (1/8)
time_for_relax = duration_of_break * (1/4)
total_time = duration_of_episode + time_for_relax + time_for_lunch
if duration_of_break >= total_time:
    time_left = duration_of_break - total_time
    print(f"You have enough time to watch {name_of_series} and left with {math.ceil(time_left)} minutes free time.")
elif duration_of_break < total_time:
    time_needed = total_time - duration_of_break
    print(f"You don't have enough time to watch {name_of_series}, you need {math.ceil(time_needed)} more minutes.")