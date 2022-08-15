from collections import deque

working_bees = deque(map(int, input().split()))
nectar = [int(i) for i in input().split()]
making_process = deque(input().split())

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}
result = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        working_bees.appendleft(current_bee)
        continue

    if current_nectar == 0:
        continue

    current_symbol = making_process.popleft()
    result += abs(operations[current_symbol](current_bee, current_nectar))

print(f"Total honey made: {result}")

if working_bees:
    print(f"Bees left: {', '.join([str(i) for i in working_bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(i) for i in nectar])}")

