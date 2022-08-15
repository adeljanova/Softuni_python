data = input()

forces = {}

while data != "Lumpawaroo":
    split_data = data.split(" | ")
    if len(split_data) > 1:
        user, side = split_data
        if user in forces:
            continue
        if user not in forces:
            forces[user] = [side]
        else:
            forces[user].append(side)
    else:
        split_data = data.split(" -> ")
        side, user = split_data
        if user in forces:
            forces[user] = [side]
        elif user not in forces:
            forces[user].append(side)
        else:
            forces[user] = [side]
            print(f"{user} joins the {side} side!")
    data = input()

output = [print(f"Side: {side}, Members: {len(forces)}") for side in forces.keys()]
for key, value in forces.items():
    if key:
        print(f"! {value}")
