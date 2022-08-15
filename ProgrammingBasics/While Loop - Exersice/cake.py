length = int(input())
width = int(input())
cake = length * width
sum_pieces = 0
new_pieces = input()
while new_pieces != "STOP":
    sum_pieces += int(new_pieces)
    if sum_pieces >= cake:
        break
    new_pieces = input()
difference = abs(cake - sum_pieces)
if new_pieces == "STOP" and sum_pieces < cake:
    print(f"{difference} pieces are left." )
else:
    print(f"No more cake left! You need {difference} pieces more.")