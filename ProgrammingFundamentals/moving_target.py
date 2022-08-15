sequence_of_targets = list(map(int, input().split()))

command = input()
while command != "End":
    command = command.split()
    line = command[0]
    index = int(command[1])
    value = int(command[2])
    if line == "Shoot" and index >= 0 and index < len(sequence_of_targets):
        sequence_of_targets[index] -= value
        if sequence_of_targets[index] <= 0:
            sequence_of_targets.pop(index)
    elif line == "Add":
        if index >= 0 and index < len(sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif line == "Strike":
        if index + value < len(sequence_of_targets) and index - value >= 0:
            sequence_of_targets = sequence_of_targets[:index - value] + sequence_of_targets[index + value + 1:]
        else:
            print("Strike missed!")
    command = input()
sequence_of_targets_as_string = [str(i) for i in sequence_of_targets]
print("|".join(sequence_of_targets_as_string))
