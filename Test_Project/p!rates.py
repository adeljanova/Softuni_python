data = input()

data_saver = {}
while data != "Sail":
    city, population, gold = data.split("||")
    population, gold = int(population), int(gold)
    if city not in data_saver:
        data_saver[city] = [population, gold]
    else:
        data_saver[city][0] += population
        data_saver[city][1] += gold
    data = input()

info = input()

while info != "End":
    split_info = info.split("=>")
    command, town = split_info[0], split_info[1]
    if command == "Plunder":
        people, gold = int(split_info[2]), int(split_info[3])
        data_saver[town][0] -= people
        data_saver[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if data_saver[town][0] <= 0 or data_saver[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del data_saver[town]
    elif command == "Prosper":
        gold = int(split_info[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            data_saver[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {data_saver[town][1]} gold.")
    info = input()

if not data_saver:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(data_saver)} wealthy settlements to go to:")
    output = [print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg") for key, value in data_saver.items()]
