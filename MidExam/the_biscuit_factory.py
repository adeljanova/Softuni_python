import math

biscuits_per_day_worker = int(input())
workers_count = int(input())
total_competing_factory_biscuits = int(input())

total_biscuits = 0
for day in range(1, 31):
    if day % 3 == 0:
        total_biscuits += ((biscuits_per_day_worker * workers_count) * 0.75)
        total_biscuits = math.floor(total_biscuits)
    else:
        total_biscuits += (biscuits_per_day_worker * workers_count)

print(f"You have produced {total_biscuits} biscuits for the past month.")

difference = abs(total_biscuits - total_competing_factory_biscuits)
diff_percent = (difference / total_competing_factory_biscuits) * 100
if total_biscuits > total_competing_factory_biscuits:
    print(f"You produce {diff_percent:.2f} percent more biscuits.")
else:
    print(f"You produce {diff_percent:.2f} percent less biscuits.")