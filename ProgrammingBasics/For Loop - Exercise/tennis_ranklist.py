import math

num_games = int(input())
start_points = int(input())
stage_points = 0
total_points = 0
w = 0
percentage = 0
for i in range(num_games):
    tur_stage = input()
    if tur_stage == "W":
        stage_points += 2000
        w += 1
        percentage = w / num_games * 100
    elif tur_stage == "F":
        stage_points += 1200
    elif tur_stage == "SF":
        stage_points += 720
total_points = start_points + stage_points
print(f"Final points: {total_points}")
average = stage_points / num_games
print(f"Average points: {math.floor(average)}")
print(f"{percentage:.2f}%")