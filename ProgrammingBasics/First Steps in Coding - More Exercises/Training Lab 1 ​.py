w = float(input())
h = float(input())
3 <= h <= w <= 100
for_height = (h * 100) - 100
desks_on_roll_h = for_height // 70
for_width = (w * 100)
desks_on_roll_w = for_width // 120
total_desks = (desks_on_roll_w * desks_on_roll_h) - 3
print(total_desks)
