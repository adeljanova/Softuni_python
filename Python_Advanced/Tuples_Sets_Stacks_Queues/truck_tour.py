from collections import deque

petrol_pumps = int(input())
station = 0
queue = deque()
for _ in range(petrol_pumps):
    petrol, kilometres = input().split()
    queue.append(f"{petrol} - {kilometres}")

for item in queue:
    petrol, kilometres = item.split(" - ")
    if int(petrol) > int(kilometres):
        station = queue.index(item)
        break
print(station)

