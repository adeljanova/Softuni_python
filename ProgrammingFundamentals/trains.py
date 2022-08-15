wagons = int(input())
train = [0 for i in range(wagons)]

command = input()
while command != "End":
    command = command.split()
    if "add" in command:
        people = int(command[1])
        train[(len(train) - 1)] += people
    elif "insert" in command:
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif "leave" in command:
        index = int(command[1])
        people = int(command[2])
        train[index] -= people
    command = input()
print(train)
