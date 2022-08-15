num_floors = int(input())
num_rooms = int(input())
room_nums = ""
for floors in range(num_floors, 0, -1):
    for rooms in range(0, num_rooms):
        num_of_rooms = floors * 10 + rooms
        if floors == num_floors:
            print(f"L{num_of_rooms} ", end="")
        elif floors % 2 != 0:
            room_nums += f"A{num_of_rooms} "
        else:
            room_nums += f"O{num_of_rooms} "
    print(room_nums)
    room_nums = ""