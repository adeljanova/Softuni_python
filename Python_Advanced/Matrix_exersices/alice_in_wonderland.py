size = int(input())
matrix = []

alice_row = 0
alice_col = 0
for row in range(size):
    line = input().split()
    for i in range(len(line)):
        if line[i] == "A":
            alice_row = row
            alice_col = i
    matrix.append(line)

tea_bags = 0
command = input()
matrix[alice_row][alice_col] = "*"

while True:

    if command == "down":
        alice_row += 1
    elif command == "up":
        alice_row -= 1
    elif command == "left":
        alice_col -= 1
    elif command == "right":
        alice_col += 1

    if alice_row < 0:
        alice_row += 1
        break
    elif alice_row > size - 1:
        alice_row -= 1
        break
    elif alice_col < 0:
        alice_col += 1
        break
    elif alice_col > size - 1:
        alice_col -= 1
        break

    if matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        break
    else:
        if matrix[alice_row][alice_col].isdigit():
            tea_bags += int(matrix[alice_row][alice_col])
            matrix[alice_row][alice_col] = "*"
            if tea_bags >= 10:
                break
    matrix[alice_row][alice_col] = "*"
    command = input()

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for line in matrix:
    print(*line, sep=" ")