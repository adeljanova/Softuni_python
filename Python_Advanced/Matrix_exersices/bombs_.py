n = int(input())
matrix = []
coordinates = []
sum = 0
active_sells = 0

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for i in input().split(" "):
    x, y = i.split(",")
    coordinates.append([int(x), int(y)])

for bomb in coordinates:
    current_bomb = matrix[bomb[0]][bomb[1]]
    for row in range(n):
        for col in range(n):
            if matrix[row][col] > 0:
                if row == bomb[0]-1:
                    if col == bomb[1]-1 or col == bomb[1] or col == bomb[1]+1:
                        matrix[row][col] -= current_bomb
                elif row == bomb[0]:
                    if col == bomb[1]-1 or col == bomb[1]+1:
                        matrix[row][col] -= current_bomb
                elif row == bomb[0]+1:
                    if col == bomb[1]-1 or col == bomb[1] or col == bomb[1]+1:
                        matrix[row][col] -= current_bomb
        matrix[bomb[0]][bomb[1]] = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            active_sells += 1
            sum += matrix[i][j]

print(f'Alive cells: {active_sells}')
print(f"Sum: {sum}")
for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=" ")
    print()
