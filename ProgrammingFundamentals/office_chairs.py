num_of_rooms = int(input())

counter = 0

is_left = True
for room in range(num_of_rooms):
    command = input().split()
    num_of_chairs_as_list = [i for i in range(len(command[0]))]
    num_of_chairs = len(num_of_chairs_as_list)
    num_of_people = int(command[1])
    if num_of_chairs < num_of_people:
        print(f"{num_of_people - num_of_chairs} more chairs needed in room {room + 1}")
        is_left = False
    else:
        counter += (num_of_chairs - num_of_people)
if is_left:
    print(f"Game On, {counter} free chairs left")

