matrix = []

person_row = 0
person_col = 0
targets = 0
for row in range(5):
    line = input().split()
    matrix.append(line)
    for i in range(len(line)):
        if line[i] == "A":
            person_row = row
            person_col = i
        elif line[i] == "x":
            targets += 1

num_commands = int(input())
shoot_targets = 0
target_list = []
for _ in range(num_commands):
    data = input().split()

    if "move" in data:
        command, direction, steps = data

        if direction == "up":
            if person_row - int(steps) < 0 or matrix[person_row - int(steps)][person_col] != ".":
                continue
            else:
                person_row -= int(steps)
        elif direction == "down":
            if (person_row + int(steps)) > 4 or matrix[person_row+int(steps)][person_col] != ".":
                continue
            else:
                person_col += int(steps)
        elif direction == "right":
            if (person_col + int(steps)) > 4 or matrix[person_row][person_col + int(steps)] != ".":
                continue
            else:
                person_col += int(steps)
        elif direction == "left":
            if (person_col - int(steps)) < 0 or matrix[person_row][person_col - int(steps)] != ".":
                continue
            else:
                person_col -= int(steps)

    elif "shoot" in data:
        command, direction = data

        if direction == "up":
            for r in range(person_row, -1, -1):
                if matrix[r][person_col] == "x":
                    matrix[r][person_col] = "."
                    shoot_targets += 1
                    target_list.append([r, person_col])
                    break
        elif direction == "down":
            for r in range(person_row, 5):
                if matrix[r][person_col] == "x":
                    matrix[r][person_col] = "."
                    shoot_targets += 1
                    target_list.append([r, person_col])
                    break
        elif direction == "right":
            for c in range(person_col, 5):
                if matrix[person_row][c] == "x":
                    matrix[person_row][c] = "."
                    shoot_targets += 1
                    target_list.append([person_row, c])
                    break
        elif direction == "left":
            for c in range(person_col, -1, -1):
                if matrix[person_row][c] == "x":
                    matrix[person_row][c] = "."
                    shoot_targets += 1
                    target_list.append([person_row, c])
                    break

if shoot_targets == targets:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - shoot_targets} targets left.")

for s in target_list:
    print(s)