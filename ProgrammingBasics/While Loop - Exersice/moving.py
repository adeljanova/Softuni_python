width = int(input())
length = int(input())
height = int(input())
total_space = width * length * height
space_taking = 0
boxes = input()
while boxes != "Done":
    space_taking += int(boxes)
    if space_taking >= total_space:
        break
    boxes = input()
difference = abs(space_taking - total_space)
if boxes == "Done" and space_taking < total_space:
    print(f"{difference} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")

