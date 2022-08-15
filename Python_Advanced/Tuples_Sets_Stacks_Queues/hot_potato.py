from collections import deque

kids = deque(input().split())
counter = int(input())

while kids:
    for toss in range(counter - 1):
        kids.append(kids.popleft())
    kid_to_remove = kids.popleft()
    if kids:
        print(f"Removed {kid_to_remove}")
    else:
        print(f"Last is {kid_to_remove}")