command = input()

to_do_notes = [0 for i in range(11)]

while command != "End":
    command = command.split("-")
    importance = int(command[0]) - 1
    note = command[1]
    to_do_notes.pop(importance)
    to_do_notes.insert(importance, note)
    command = input()
result = [i for i in to_do_notes if i != 0]
print(result)

