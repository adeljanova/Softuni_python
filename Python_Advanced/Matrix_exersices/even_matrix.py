rows = int(input())
matrix = []
for _ in range(rows):
    line = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(line)

print(matrix)
