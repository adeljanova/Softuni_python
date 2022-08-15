def get_count(matrix, row, col):
    moves = [
        [row-2, col-1],
        [row-2, col+1],
        [row-1, col-2],
        [row-1, col+2],
        [row+1, col-2],
        [row+1, col+2],
        [row+2, col-1],
        [row+2, col+1]
    ]
    result = 0
    for r, c in moves:
        if (0 <= r < len(matrix) and 0 <= c < len(matrix)) and matrix[r][c] == "K":
            result += 1

    return result


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([list(input())])

knight_counter = 0
while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "0":
                continue
            count = get_count(matrix, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    matrix[knight_row][knight_col] = "0"
    knight_counter += 1
print(knight_counter)