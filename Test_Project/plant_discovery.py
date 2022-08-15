n = int(input())

information = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    if plant in information:
        information[plant] = [int(rarity)]
    else:
        information[plant] = [int(rarity)]

data = input()

while data != "Exhibition":
    command, info = data.split(": ")
    if command == "Rate":
        plant, rating = info.split(" - ")
        if plant not in information:
            print("error")
        else:
            rating = int(rating)
            information[plant].append(rating)
    elif command == "Update":
        plant, new_rarity = info.split(" - ")
        if plant not in information:
            print("error")
        else:
            new_rarity = int(new_rarity)
            information[plant][0] = new_rarity
    elif command == "Reset":
        plant = info
        if plant not in information:
            print("error")
        else:
            del information[plant][1:]
    data = input()

print("Plants for the exhibition:")

sum = 0
average = 0
for key, value in information.items():
    for index in range(len(value)):
        if len(value) > 2:
            for i in range(1, len(value)):
                sum += value[i]
            average = sum / (len(value) - 1)
            print(f"- {key}; Rarity: {value[index]}; Rating: {average:.2f}")
            break
        elif len(value) == 2:
            print(f"- {key}; Rarity: {value[index]}; Rating: {value[index+1]:.2f}")
            break
        else:
            print(f"- {key}; Rarity: {value[index]}; Rating: 0.00")
            break
