km = int(input())
day_or_night = input()
taxi_start_price = 0.70
day_taxi = 0.79 * km
night_taxi = 0.90 * km
bus_price = 0.09 * km
train_price = 0.06 * km
if km < 20:
    if day_or_night == "day":
        total_taxi = taxi_start_price + day_taxi
    elif day_or_night == "night":
        total_taxi = taxi_start_price + night_taxi
    print(f"{total_taxi:.2f}")
elif 20 <= km < 100:
    print(f"{bus_price:.2f}")
elif km >= 100:
    print(f"{train_price:.2f}")


