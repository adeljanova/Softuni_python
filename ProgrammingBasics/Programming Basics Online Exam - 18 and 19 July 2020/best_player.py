import sys

player = input()
top_goals = -sys.maxsize
best_player = ""
while player != "END":
    num_goals = int(input())
    if num_goals > top_goals:
        top_goals = num_goals
        best_player = player
    if top_goals >= 10:
        break
    player = input()
print(f"{best_player} is the best player!")
if top_goals >= 3:
    print(f"He has scored {top_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {top_goals} goals.")















