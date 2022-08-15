rows, columns = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append([x for x in input().split()])

data = input()
while data != "END":
    temp_list = []
    split_data = data.split()
    if "swap" in data and len(split_data) == 5:
        row1, col1, row2, col2 = [int(x) for x in split_data[1:]]
        if row1 < 0 or row2 < 0 or col1 < 0 or col2 < 0 or\
            row1 > rows or row2 > rows or col1 > columns or col2 > columns:
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = \
                matrix[row2][col2], matrix[row1][col1]
            for i in matrix:
                print(*i, sep=" ")
    else:
        print("Invalid input!")

    data = input()