n = int(input())
matrix = []

for i in range(n):
    line = list(input())
    matrix.append(line)

symbol = input()
location = ()
is_found = False

for i in range(n):
    for j in range(n):
        if is_found:
            break
        if symbol in matrix[i][j]:
            is_found = True
            location = (i, j)

if not is_found:
    print(f"{symbol} does not occur in the matrix")
else:
    print(location)
