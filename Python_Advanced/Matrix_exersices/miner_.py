def get_command(command, row, col):
    if command == "left":
        return row, col + 1
    elif command == "right":
        return row, col - 1
    elif command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col


n = int(input())
commands_list = input().split()
matrix = []
total_coal = 0
miner_row = 0
miner_col = 0
for row in range(n):
    line = input().split()
    matrix.append(line)
    for col in range(n):
        element = line[col]
        if element == "c":
            total_coal += 1
        elif element == "s":
            miner_row = row
            miner_col = col

end = False
for cmd in commands_list:
    next_row, next_col = get_command(cmd, miner_row, miner_col)
    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        continue

    miner_row, miner_col = next_row, next_col

    if matrix[miner_row][miner_col] == "c":
        matrix[miner_row][miner_col] = "*"
        total_coal -= 1
        if total_coal == 0:
            break
    elif matrix[miner_row][miner_col] == "e":
        end = True
        break

if total_coal == 0:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif end:
    print(f"Game over! ({miner_row}, {miner_col})")
else:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")
