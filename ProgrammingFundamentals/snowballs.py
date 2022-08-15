snowballs = int(input())
last_value = 0
last_weight = 0
last_time = 0
last_quality = 0
for i in range(1, snowballs + 1):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight_of_snowball / time_needed) ** quality
    if value > last_value:
        last_value = value
        last_weight = weight_of_snowball
        last_time = time_needed
        last_quality = quality
print(f"{last_weight} : {last_time} = {int(last_value)} ({last_quality})")