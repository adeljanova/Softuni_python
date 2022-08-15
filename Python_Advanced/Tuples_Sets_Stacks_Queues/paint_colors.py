from collections import deque

string_of_colors = deque(str(x) for x in input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

created_secondary_colors = {
    "orange": ('red', 'yellow'),
    "purple": ('red', 'blue'),
    "green": ('yellow', 'blue')
}

founded_colors = []
secondary_list = []

checker = ''

while string_of_colors:
    first = string_of_colors.popleft()
    last = string_of_colors.pop() if string_of_colors else ''

    checker = first + last
    if checker in main_colors or checker in secondary_colors:
        secondary_list.append(checker)
        continue

    checker = last + first
    if checker in main_colors or checker in secondary_colors:
        secondary_list.append(checker)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        string_of_colors.insert(len(string_of_colors) // 2, first)
    if last:
        string_of_colors.insert(len(string_of_colors) // 2, last)

for item in secondary_list:
    if item in main_colors:
        founded_colors.append(item)
    elif item in secondary_list:
        left = created_secondary_colors[item][0]
        right = created_secondary_colors[item][1]
        if (left in founded_colors or left in secondary_list) \
                and (right in founded_colors or right in secondary_list):
            founded_colors.append(item)

print(founded_colors)




