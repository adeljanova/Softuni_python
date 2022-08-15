import math

record_in_secs = float(input())
distance_in_metres = float(input())
time_for_metre = float(input())
distance_time = distance_in_metres * time_for_metre
round_down = math.floor((distance_in_metres / 50))
fifty_metres = round_down * 30
total_time = distance_time + fifty_metres
if total_time >= record_in_secs:
    print(f"No! He was {abs(total_time - record_in_secs):.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")