data = input()

player_pool = {}

while data != "Season end":
    split_data = data.split(" -> ")
    if len(split_data) > 2:
        player, position, skill = split_data
        skill = int(skill)
        if player not in player_pool:
            player_pool[player] = {}
        if position not in player_pool[player]:
            player_pool[player][position] = skill
        else:
            if player_pool[player][position] <= skill:
                player_pool[player][position] = skill
    else:
        split_data = data.split(" vs ")
        player_one, player_two = split_data
        if player_one in player_pool and player_two in player_pool:
            for position1 in player_pool[player_one].keys():
                for position2 in player_pool[player_two].keys():
                    if position1 == position2:
                        if player_pool[player_one][position1] > player_pool[player_two][position2]:
                            del player_pool[player_two]
                        elif player_pool[player_one][position1] < player_pool[player_two[position2]]:
                            del player_pool[player_one]
    data = input()

total_score = {}

for name, info in player_pool.items():
    for key, value in info.items():
        if name not in total_score:
            total_score[name] = value
        else:
            total_score[name] += value

sorted_total_score = dict(sorted(total_score.items(), key=lambda x: (-x[1], x[0])))

for name, score in sorted_total_score.items():
    print(f"{name}: {score} skill")
    for position, info in sorted(player_pool.items(), key=lambda n: n[0]):
        if name == position:
            for key, value in sorted(info.items(), key=lambda ps: (-ps[1], ps[0])):
                print(f"- {key} <::> {value}")


