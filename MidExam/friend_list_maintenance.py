friends_list = list(map(str, input().split(", ")))
line = input()

blacklist_counter = 0
lost_counter = 0
while line != "Report":
    line = line.split()
    command = line[0]
    if "Blacklist" in command:
        name = line[1]
        if name in friends_list:
            print(f"{name} was blacklisted.")
            i = friends_list.index(name)
            # friends_list = list(map(lambda x: x.replace(friends_list[i], "Blacklisted"), friends_list))
            # friends_list = friends_list[:i] + ["Blacklisted"] + friends_list[i + 1:]
            friends_list[i] = "Blacklisted"
            blacklist_counter += 1
        else:
            print(f"{name} was not found.")
    elif "Error" in command:
        index = int(line[1])
        if friends_list[index] != "Blacklisted" and friends_list[index] != "Lost":
            if 0 <= index < len(friends_list):
                print(f"{friends_list[index]} was lost due to an error.")
                friends_list[index] = "Lost"
                lost_counter += 1
    elif "Change" in command:
        index = int(line[1])
        new_name = line[2]
        if 0 <= index < len(friends_list):
            print(f"{friends_list[index]} changed his username to {new_name}.")
            # friends_list[index] = new_name
            friends_list.pop(index)
            friends_list.insert(index, new_name)
    line = input()

print(f"Blacklisted names: {blacklist_counter}")
print(f"Lost names: {lost_counter}")
print(" ".join(friends_list))