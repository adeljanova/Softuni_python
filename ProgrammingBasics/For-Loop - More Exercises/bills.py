months = int(input())
total_water = months * 20
total_internet = months * 15
evn = 0
for month in range(months):
    electricity = float(input())
    evn += electricity
total_electricity = evn
total_others = (total_water + total_internet + total_electricity) * 1.2
average = (total_others + total_electricity + total_water + total_internet) / months
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average:.2f} lv")