import math

group_size = int(input())
days = int(input())
earnings = 0
for i in range(1, days + 1):
    if i % 15 == 0:
        group_size += 5
    if i % 10 == 0:
        group_size -= 2
    earnings += 50 - 2 * group_size
    if i % 3 == 0:
        earnings -= 3 * group_size
    if i % 5 == 0:
        earnings += 20 * group_size
        if i % 3 == 0:
            earnings -= 2 * group_size
coins = math.floor(earnings / group_size)
print(f"{group_size} companions received {coins} coins each.")