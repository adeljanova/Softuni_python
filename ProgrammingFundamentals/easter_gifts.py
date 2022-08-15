name_of_gifts = input().split()
command = input()

while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for index in range(len(name_of_gifts)):
            if command[1] in name_of_gifts[index]:
                name_of_gifts[index] = "None"
    elif "Required" in command:
        for index in range(len(name_of_gifts)):
            if index == int(command[2]):
                name_of_gifts[index] = command[1]
    elif "JustInCase" in command:
        name_of_gifts[-1] = command[1]
    command = input()
while "None" in name_of_gifts:
    name_of_gifts.remove("None")
for i in name_of_gifts:
    print(i, end=" ")