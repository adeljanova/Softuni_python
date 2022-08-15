entry = input()

phonebook = {}

while len(entry) > 2:
    name, number = entry.split("-")
    if name not in phonebook:
        phonebook[name] = number
    else:
        phonebook[name] = number
    entry = input()

n = int(entry)

for _ in range(n):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
