from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = input()
snake_as_str = [x for x in snake]
matrix = []
counter = 0
print(len(snake))
for row in range(rows):
    line = deque()
    if row % 2 == 0:
        for col in range(columns):
            print(counter % len(snake))
            line.append(snake[counter % len(snake)])
            counter += 1
        matrix.append(line)
    else:
        for col in range(columns - 1, -1, -1):
            print(counter % len(snake))
            line.appendleft(snake[counter % len(snake)])
            counter += 1
        matrix.append(line)

[print(*line, sep="") for line in matrix]




