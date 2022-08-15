plane_luggage = float(input())
command = input()
total_luggage = 0
counter = 0
while command != "End":
    command = float(command)
    luggage = command
    counter += 1
    if counter % 3 == 0:
        luggage += luggage * 0.1
    total_luggage += luggage
    if plane_luggage < total_luggage:
        counter -= 1
        print("No more space!")
        break
    command = input()
if command == "End":
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {counter} suitcases loaded.")



