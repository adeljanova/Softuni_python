n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

data = input()
while data != "END":
    command, row, col, value = data.split()
    if 0 <= int(row) < n and 0 <= int(col) < n:
        if command == "Add":
            matrix[int(row)][int(col)] += int(value)
        elif command == "Subtract":
            matrix[int(row)][int(col)] -= int(value)
    else:
        print("Invalid coordinates")
    data = input()
for row in matrix:
    print(*row, sep=" ")