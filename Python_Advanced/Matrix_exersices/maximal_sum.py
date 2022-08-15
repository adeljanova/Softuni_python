rows, columns = [int(x) for x in input().split()]
matrix = []
max_matrix = []
max_sum = float('-inf')
for i in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    current_sum = 0
    current_matrix = []
    for col in range(columns - 2):
        current_matrix = [matrix[row][col], matrix[row][col+1], matrix[row][col+2],
                          matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2],
                          matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]
        current_sum = sum(current_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = current_matrix.copy()
print(f"Sum = {max_sum}")
print(max_matrix[0], max_matrix[1], max_matrix[2])
print(max_matrix[3], max_matrix[4], max_matrix[5])
print(max_matrix[6], max_matrix[7], max_matrix[8])
