num_computers = int(input())
num_sells = 0
average_raiting = 0
sells = 0
total_sells = 0
for i in range(1, num_computers + 1):
    sell_raiting = int(input())
    sell_raiting_as_string = str(sell_raiting)
    sells = int(sell_raiting_as_string[0] + sell_raiting_as_string[1])
    if int(sell_raiting_as_string[2]) == 2:
        sells = 0
        average_raiting += 2
    elif int(sell_raiting_as_string[2]) == 3:
         sells -= int(sells) * 0.5
         average_raiting += 3
    elif int(sell_raiting_as_string[2]) == 4:
        sells -= int(sells) * 0.3
        average_raiting += 4
    elif int(sell_raiting_as_string[2]) == 5:
         sells -= int(sells) * 0.15
         average_raiting += 5
    elif int(sell_raiting_as_string[2]) == 6:
        sells = sells
        average_raiting += 6
    total_sells += sells
    num_sells += 1
average_raiting /= num_sells
print(f"{total_sells:.2f}")
print(f"{average_raiting:.2f}")




