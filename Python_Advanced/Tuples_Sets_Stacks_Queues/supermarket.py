from collections import deque

data = input()

queue = deque()
while data != "End":
    if data == "Paid":
        for pr in queue:
            print(pr)
        queue = []
    else:
        queue.append(data)
    data = input()
print(f"{len(queue)} people remaining.")