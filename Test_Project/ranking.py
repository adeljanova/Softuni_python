data = input()

data_saver = {}
while data != "end of contests":
    pre_contest, pass_for_contest = data.split(":")
    data_saver[pre_contest] = pass_for_contest
    data = input()

expanded_data = input()

ranking_dict = {}

is_valid = False
is_correct = False
while expanded_data != "end of submissions":
    contest, password, username, points = expanded_data.split("=>")
    points = int(points)
    if contest in data_saver:
        is_valid = True

    if is_valid:
        if password in data_saver[contest]:
            is_correct = True

    if is_valid and is_correct:
        if username not in ranking_dict:
            ranking_dict[username] = {}
            ranking_dict[username][contest] = points
        else:
            if contest not in ranking_dict[username]:
                ranking_dict[username][contest] = points
            else:
                if ranking_dict[username][contest] < points:
                    ranking_dict[username][contest] = points
    is_valid = False
    is_correct = False
    expanded_data = input()

# points_dict = {}
#
# for contest, info in ranking_dict.items():
#     for key, value in info.items():
#         if value not in points_dict:
#             points_dict[key] = value
#         else:
#             points_dict[key] += value

temp_points = 0
top_points = 0
top_candidate = ''

for candidate in ranking_dict.keys():
    for contest, points in ranking_dict[candidate].items():
        temp_points += points
    if temp_points > top_points:
        top_points = temp_points
        top_candidate = candidate
    temp_points = 0

print(f"Best candidate is {top_candidate} with total {top_points} points.")

print("Ranking:")
for user in sorted(ranking_dict.keys()):
    print(user)
    for contest, points in sorted(ranking_dict[user].items(), key=lambda p: -p[1]):
        print(f"#  {contest} -> {points}")