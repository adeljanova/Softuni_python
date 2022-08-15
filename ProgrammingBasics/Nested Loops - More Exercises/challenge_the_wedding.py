men = int(input())
women = int(input())
max_tables = int(input())
counter = 0
for place1 in range(1, men + 1):
    for place2 in range(1, women + 1):
        print(f"({place1} <-> {place2})", end=" ")
        counter += 1
        if counter == max_tables:
            break
    if counter == max_tables:
        break