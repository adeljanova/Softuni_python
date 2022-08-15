from collections import deque

quantity_water = int(input())

name = input()
queue = deque()
while name != "Start":
    queue.append(name)
    name = input()

data = input()

while data != "End":
    if data.startswith("refill"):
        split_data = data.split()
        quantity_water += int(split_data[1])
    else:
        current_water = int(data)
        if current_water <= quantity_water:
            print(f"{queue[0]} got water")
            queue.popleft()
            quantity_water -= current_water
        else:
            print(f"{queue[0]} must wait")
            queue.popleft()
    data = input()

print(f"{quantity_water} liters left")