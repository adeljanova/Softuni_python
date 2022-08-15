from collections import deque

data = input().split(";")
start_hour, start_minute, start_second = input().split(":")
start_hour, start_minute, start_second = int(start_hour), int(start_minute), int(start_second)

robot_queue = deque(data)

product = input()
current_robot_queue = deque()
processing_queue = deque()

while product != "End":

    if robot_queue:
        current_robot = robot_queue.popleft()
        current_robot_queue.append(current_robot)
        start_second += 1
        if start_second < 10:
            start_second = "0" + str(start_second)
        if int(start_second) > 59:
            start_minute += 1
            start_second = 0
        if start_minute < 10:
            start_minute = "0" + str(start_minute)
        if int(start_minute) > 59:
            start_hour += 1
            start_minute = 0
        if start_hour < 10:
            start_hour = "0" + str(start_hour)
        print(f"{current_robot} - {product} [{start_hour}:{start_minute}:{start_second}]")
        start_hour, start_minute, start_second = int(start_hour), int(start_minute), int(start_second)
    else:
        pass
    product = input()
