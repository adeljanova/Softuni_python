rows = int(input())
matrix = []
sum = 0

for i in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for i in range(rows):
    for j in range(rows):
        if i == j:
            sum += matrix[i][j]

print(sum)
