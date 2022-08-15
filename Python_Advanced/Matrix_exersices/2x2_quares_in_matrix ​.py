rows, columns = [int(x) for x in input().split()]
matrix = []
counter = 0

for i in range(rows):
    matrix.append([str(x) for x in input().split()])

for row in range(rows-1):
    for col in range(columns-1):
        current_sell = matrix[row][col]
        if current_sell == matrix[row][col+1] and\
            current_sell == matrix[row+1][col] and\
            current_sell == matrix[row+1][col+1]:
            counter += 1
print(counter)