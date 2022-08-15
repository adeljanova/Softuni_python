data = input()

contests = {}
individual_statistics = {}

while data != "no more time":
    username, contest, points = data.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = points
    else:
        if contests[contest][username] < points:
            contests[contest][username] = points
    data = input()

for key, info in contests.items():
    for key1, value in info.items():
        if key1 not in individual_statistics:
            individual_statistics[key1] = value
        else:
            individual_statistics[key1] += value

counter = 1
for cont, value in contests.items():
    print(f"{cont}: {len(contests[cont])} participants")
    for user, points_ in (sorted(contests[cont].items(), key=lambda p: (-p[1], p[0]))):
        print(f"{counter}. {user} <::> {points_}")
        counter += 1
    counter = 1

print("Individual standings:")
for user, points in sorted(individual_statistics.items(), key=lambda p: (-p[1], p[0])):
    print(f"{counter}. {user} -> {points}")
    counter += 1


