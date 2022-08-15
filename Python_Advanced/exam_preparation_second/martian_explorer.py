from collections import deque


rover_row = 0
rover_col = 0
matrix = []

for row in range(6):
    line = [x for x in input().split()]
    for col in range(len(line)):
        if line[col] == "E":
            rover_row = row
            rover_col = col
    matrix.append(line)

commands = deque(input().split(", "))
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

while commands:
    current_move = commands.popleft()
    if current_move == "right":
        if rover_col < 5:
            rover_col += 1
        else:
            rover_col = 0
    elif current_move == "left":
        if rover_col == 0:
            rover_col = 5
        else:
            rover_col -= 1
    elif current_move == "up":
        if rover_row == 0:
            rover_row = 5
        else:
            rover_row -= 1
    elif current_move == "down":
        if rover_row < 5:
            rover_row += 1
        else:
            rover_row = 0

    if matrix[rover_row][rover_col] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")



