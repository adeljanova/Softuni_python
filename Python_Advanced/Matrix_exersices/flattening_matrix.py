rows = int(input())
matrix = []

for i in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

flattened_matrix = [x for line in matrix for x in line]
print(flattened_matrix)