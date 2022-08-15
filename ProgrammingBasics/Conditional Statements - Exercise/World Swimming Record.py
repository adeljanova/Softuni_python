import math

record_in_secs = float(input())
distance_in_metres = float(input())
secs_for_swimming_one_metre = float(input())
total_time_for_swimming_without_delay = distance_in_metres * secs_for_swimming_one_metre
distance_with_delay = math.floor(distance_in_metres / 15) * 12.5
total_time_for_swimming_with_delay = distance_with_delay + total_time_for_swimming_without_delay
if record_in_secs > total_time_for_swimming_with_delay:
    print(f"Yes, he succeeded! The new world record is {total_time_for_swimming_with_delay:.2f} seconds.")
elif record_in_secs <= total_time_for_swimming_with_delay:
    secs_short = total_time_for_swimming_with_delay - record_in_secs
    print(f"No, he failed! He was {secs_short:.2f} seconds slower.")