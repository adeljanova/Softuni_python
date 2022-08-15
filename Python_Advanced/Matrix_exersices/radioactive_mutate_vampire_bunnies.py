rows, columns = [int(x) for x in input().split()]
matrix = []

player_row = 0
player_col = 0
bunny_list = []
for row in range(rows):
    line = list(input())
    for i in range(len(line)):

        if line[i] == "P":
            player_row, player_col = row, i

        elif line[i] == "B":
            bunny_list.append((row, i))
    matrix.append(line)

command_line = list(input())
is_dead = False
win = False

for cmd in command_line:
    matrix[player_row][player_col] = "."

    if cmd == "L":
        player_col -= 1
    elif cmd == "R":
        player_col += 1
    elif cmd == "U":
        player_row -= 1
    elif cmd == "D":
        player_row += 1

    for bunny in bunny_list:

        if 0 < bunny[1] and matrix[bunny[0]][bunny[1]-1] == ".":
            matrix[bunny[0]][bunny[1] - 1] = "B"

        if bunny[1] < columns - 1 and matrix[bunny[0]][bunny[1]+1] == ".":
            matrix[bunny[0]][bunny[1] + 1] = "B"

        if 0 < bunny[0] and matrix[bunny[0] - 1][bunny[1]] == ".":
            matrix[bunny[0]-1][bunny[1]] = "B"

        if bunny[0] < rows - 1 and matrix[bunny[0]+1][bunny[1]] == ".":
            matrix[bunny[0]+1][bunny[1]] = "B"

    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "B" and ((r, c) not in bunny_list):
                bunny_list.append((r, c))

    if player_row < 0:
        player_row += 1
        win = True
        break
    elif player_row > rows - 1:
        player_row -= 1
        win = True
        break
    elif player_col < 0:
        player_col += 1
        win = True
        break
    elif player_col > columns - 1:
        player_col -= 1
        win = True
        break

    if matrix[player_row][player_col] == ".":
        matrix[player_row][player_col] = "P"

    elif matrix[player_row][player_col] == "B":
        is_dead = True
        break

for line in matrix:
    print(*line, sep='')

if is_dead:
    print(f"dead: {player_row} {player_col}")
elif win:
    print(f"won: {player_row} {player_col}")
else:
    print(f"won: {player_row} {player_col}")




