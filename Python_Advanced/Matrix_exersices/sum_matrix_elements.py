rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for i in range(rows):
    lines = [int(x) for x in input().split(', ')]
    matrix.append(lines)
sum = 0
for i in range(len(matrix)):
    for j in matrix[i]:
        sum += j
print(sum)
print(matrix)