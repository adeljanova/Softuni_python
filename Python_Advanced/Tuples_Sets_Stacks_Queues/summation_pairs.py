from collections import deque

numbers = deque(map(int, input().split()))
target = int(input())

unique_pairs = set()
iterations = 0
while True:

    if not numbers:
        break
    temp_number = numbers.popleft()
    for number in numbers:
        if number + temp_number == target:
            unique_pairs.add((temp_number, number))
            print(f"{temp_number} + {number} = {target}")
        iterations += 1
print(f"Iterations done: {iterations}")
[print(pair) for pair in unique_pairs]