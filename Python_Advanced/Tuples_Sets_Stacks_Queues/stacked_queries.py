from collections import deque

n = int(input())

stack = []
for _ in range(n):
    data = input().split()
    command = data[0]
    if command == "1":
        number = int(data[1])
        stack.append(number)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

output = deque()
for el in stack:
    output.appendleft(str(el))
print(", ".join(output))