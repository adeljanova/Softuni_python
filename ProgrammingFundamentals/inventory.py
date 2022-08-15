items = list(map(str, input().split(", ")))

command = input()

while command != "Craft!":
    command = command.split(" - ")
    phrase = str(command[0])
    item = str(command[1])
    if "Collect" in phrase:
        if item not in items:
            items.append(item)
    elif "Drop" in phrase and item in items:
        items.remove(item)
    elif "Combine Items" in phrase:
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        for i in range(len(items)):
            if old_item in items[i]:
                if (i + 1) > len(items) - 1:
                    i = 0, items.insert(i, new_item)
                    break
                else:
                    items.insert(i + 1, new_item)
                    break
    elif "Renew" in phrase:
        for i in range(len(items)):
            if item in items[i]:
                items.remove(item), items.append(item)
                break
    command = input()
print(", ".join(items))