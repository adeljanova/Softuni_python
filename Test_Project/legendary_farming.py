data = input()

key_materials = {'shards': "Shadowmourne", 'fragments': "Valanyr", 'motes': "Dragonwrath"}
winning_dict = {"shards": 0, "fragments": 0, "motes": 0}

while winning_dict["shards"] < 250 or winning_dict["fragments"] < 250 or winning_dict["motes"] < 250:
    data = data.split()
    for item in range(0, len(data), 2):
        quantity = int(data[item])
        type_material = data[item+1].lower()
        if type_material in winning_dict:
            winning_dict[type_material] += quantity
    data = input()

if winning_dict["shards"] >= 250:
    print("Shadowmourne obtained!")
elif winning_dict["fragments"] >= 250:
    print("Valanyr obtained!")
elif winning_dict["motes"] >= 250:
    print("Dragonwarth obtained!")




