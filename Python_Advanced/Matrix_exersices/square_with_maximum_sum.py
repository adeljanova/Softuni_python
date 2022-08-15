rows, columns = [int(x) for x in input().split(", ")]
matrix = []
sum_matrix = 0
max_matrix = []

for i in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)

for row in range(rows - 1):
    for col in range(columns - 1):
        sub_matrix = [matrix[row][col], matrix[row][col+1],
                      matrix[row+1][col], matrix[row+1][col+1]]
        curren_sum = sum(sub_matrix)

        if curren_sum > sum_matrix:
            sum_matrix = curren_sum
            max_matrix = sub_matrix.copy()

print(max_matrix[0], max_matrix[1])
print(max_matrix[2], max_matrix[3])
print(sum_matrix)
