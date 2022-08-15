presents = int(input())
size = int(input())

matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0
for row in range(size):
    line = input().split()
    for col in range(len(line)):
        if line[col] == "S":
            santa_row = row
            santa_col = col
        elif line[col] == "V":
            nice_kids += 1
    matrix.append(line)

command = input()
nice_kids_presents = 0
while command != "Christmas morning":

    matrix[santa_row][santa_col] = "-"
    if command == "up":
        if santa_row - 1 >= 0:
            santa_row -= 1
    elif command == "down":
        if santa_row + 1 < size:
            santa_row += 1
    elif command == "right":
        if santa_col + 1 >= 0:
            santa_col += 1
    elif command == "left":
        if santa_col - 1 < size:
            santa_col -= 1

    if matrix[santa_row][santa_col] == "X":
        continue
    elif matrix[santa_row][santa_col] == "V":
        nice_kids_presents += 1
        nice_kids -= 1
        presents -= 1
    elif matrix[santa_row][santa_col] == "C":
        if santa_row - 1 >= 0:
            if matrix[santa_row - 1][santa_col] == "V":
                nice_kids_presents += 1
                nice_kids -= 1
                presents -= 1
            elif matrix[santa_row - 1][santa_col] == "X":
                presents -= 1
            matrix[santa_row-1][santa_col] = "-"
        if santa_row + 1 < size:
            if matrix[santa_row + 1][santa_col] == "V":
                nice_kids_presents += 1
                nice_kids -= 1
                presents -= 1
            elif matrix[santa_row + 1][santa_col] == "X":
                presents -= 1
            matrix[santa_row+1][santa_col] = "-"
        if santa_col - 1 >= 0:
            if matrix[santa_row][santa_col - 1] == "V":
                nice_kids_presents += 1
                nice_kids -= 1
                presents -= 1
            elif matrix[santa_row][santa_col - 1] == "X":
                presents -= 1
            matrix[santa_row][santa_col-1] = "-"
        if santa_col + 1 < size:
            if matrix[santa_row][santa_col + 1] == "V":
                nice_kids_presents += 1
                nice_kids -= 1
                presents -= 1
            elif matrix[santa_row][santa_col + 1] == "X":
                presents -= 1
            matrix[santa_row][santa_col+1] = "-"
    matrix[santa_row][santa_col] = "S"
    if not presents:
        break
    command = input()

if not presents and nice_kids > 0:
    print("Santa ran out of presents!")

for line in matrix:
    print(*line, sep=" ")

if nice_kids:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")

