stadium_capacity = int(input())
num_fans = int(input())
fan_a = 0
fan_b = 0
fan_v = 0
fan_g = 0
for fan in range(num_fans):
    sector = input()
    if sector == "A":
        fan_a += 1
    elif sector == "B":
        fan_b += 1
    elif sector == "V":
        fan_v += 1
    elif sector == "G":
        fan_g += 1

percent_a = fan_a / num_fans * 100
percent_b = fan_b / num_fans * 100
percent_v = fan_v / num_fans * 100
percent_g = fan_g / num_fans * 100
percent_total = num_fans / stadium_capacity * 100
print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_total:.2f}%")