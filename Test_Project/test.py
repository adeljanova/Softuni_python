spell = input()
data = input()

while data != "Abracadabra":
    split_data = data.split()
    command = split_data[0]
    if command == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif command == "Illusion":
        index = int(split_data[1])
        letter = split_data[2]
        if index > len(spell):
            print("The spell was too weak")
        else:
            spell = spell.replace(spell[index], letter)
            print("Done!")
    elif command == "Divination":
        first_substring = split_data[1]
        second_substring = split_data[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
    elif command == "Alteration":
        substring = split_data[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")
    data = input()