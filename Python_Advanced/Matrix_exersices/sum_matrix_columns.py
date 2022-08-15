rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for i in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)
sum = []
for i in range(columns):
    column_sum = 0
    for j in range(rows):
        column_sum += matrix[j][i]
    sum.append(column_sum)
for el in sum:
    print(el)