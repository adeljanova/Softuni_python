import re

text = input()
total_points = 0
pattern = r"(?P<symbols>\=|\/)(?P<word>[A-Z][A-Za-z]{2,})(?P=symbols)"
matches = re.findall(pattern, text)

match_list = []
for i in range(len(matches)):
    match_list.append(matches[i][1])

for i in match_list:
    total_points += len(i)
print(f"Destinations: {', '.join(match for match in match_list)}")
print(f"Travel Points: {total_points}")
