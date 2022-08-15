n = int(input())
matrix = []

for _ in range(n):
    matrix.append([x for x in input().split()])

bunny_row = 0
bunny_col = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "B":
            bunny_row = row
            bunny_col = col

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

best_sum = 0
best_dir = ""
best_path = []
for direction in directions:
    current_sum = 0
    curr_path = []
    row, col = directions[direction](bunny_row, bunny_col)

    while 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] != "X":
        current_sum += int(matrix[row][col])
        curr_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum:
        best_sum = current_sum
        best_dir = direction
        best_path = curr_path

print(best_dir)
for row in range(len(best_path)):
    print(best_path[row])
print(best_sum)