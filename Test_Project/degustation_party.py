data = input()

guest_list = {}
counter = 0
while data != "Stop":
    command, guest, meal = data.split("-")
    if command == "Like":
        if guest not in guest_list:
            guest_list[guest] = [meal]
        else:
            if meal not in guest_list[guest]:
                guest_list[guest] += [meal]
    elif command == "Dislike":
        if guest not in guest_list:
            print(f"{guest} is not at the party.")
        else:
            if meal not in guest_list[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")
                for value in guest_list.values():
                    for item in value:
                        if item == meal:
                            value.remove(meal)
                counter += 1
    data = input()

for key, value in guest_list.items():
    print(f"{key}: {', '.join(value)}")

print(f"Unliked meals: {counter}")