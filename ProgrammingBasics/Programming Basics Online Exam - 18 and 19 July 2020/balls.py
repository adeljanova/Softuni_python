import math

num_balls = int(input())
counter_red = 0
counter_orange = 0
counter_yellow = 0
counter_white = 0
counter_black = 0
counter_others = 0
points_red = 0
points_orange = 0
points_yellow = 0
points_white = 0
points_black = 0
total_points = 0
for i in range(num_balls):
    color = input()
    if color == "red":
        counter_red += 1
        points_red = 5
        total_points += points_red
    elif color == "orange":
        counter_orange += 1
        points_orange = 10
        total_points += points_orange
    elif color == "yellow":
        counter_yellow += 1
        points_yellow = 15
        total_points += points_yellow
    elif color == "white":
        counter_white += 1
        points_white = 20
        total_points += points_white
    elif color == "black":
        counter_black += 1
        points_black = math.floor(total_points / 2)
        total_points = points_black
    else:
        counter_others += 1

print(f"Total points: {total_points}")
print(f"Points from red balls: {counter_red}")
print(f"Points from orange balls: {counter_orange}")
print(f"Points from yellow balls: {counter_yellow}")
print(f"Points from white balls: {counter_white}")
print(f"Other colors picked: {counter_others}")
print(f"Divides from black balls: {counter_black}")
