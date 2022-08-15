def get_command(row, col, cmd):
    if cmd == "up":
        if row - 1 >= 0:
            row -= 1
    elif cmd == "down":
        if row + 1 < size:
            row += 1
    elif cmd == "right":
        if col + 1 >= 0:
            col += 1
    elif cmd == "left":
        if col - 1 < size:
            col -= 1
    return row, col


def cookie_present(row, col, nice_pres, nice_kid, present):
    if row - 1 >= 0:
        if matrix[row - 1][col] == "V":
            nice_pres += 1
            nice_kid -= 1
            present -= 1
        elif matrix[row - 1][col] == "X":
            present -= 1
        matrix[row - 1][col] = "-"
    if row + 1 < size:
        if matrix[row + 1][col] == "V":
            nice_pres += 1
            nice_kid -= 1
            present -= 1
        elif matrix[row + 1][col] == "X":
            present -= 1
        matrix[row + 1][col] = "-"
    if col - 1 >= 0:
        if matrix[row][col - 1] == "V":
            nice_pres += 1
            nice_kid -= 1
            present -= 1
        elif matrix[row][col - 1] == "X":
            present -= 1
        matrix[row][col - 1] = "-"
    if col + 1 < size:
        if matrix[row][col + 1] == "V":
            nice_pres += 1
            nice_kid -= 1
            present -= 1
        elif matrix[row][col + 1] == "X":
            present -= 1
        matrix[row][col + 1] = "-"
    return row, col, nice_pres, nice_kid, present


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
    get_command(santa_row, santa_col, command)

    if matrix[santa_row][santa_col] == "X":
        continue
    elif matrix[santa_row][santa_col] == "V":
        nice_kids_presents += 1
        nice_kids -= 1
        presents -= 1
    elif matrix[santa_row][santa_col] == "C":
        cookie_present(santa_row, santa_col, nice_kids_presents, nice_kids, presents)
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
