n = int(input())

set_one = set()
set_two = set()
lenght = 0
output = set()
for _ in range(n):
    data = input().split("-")
    first_start, first_end = map(int, data[0].split(","))
    second_start, second_end = map(int, data[1].split(","))

    for i in range(first_start, first_end+1):
        set_one.add(i)
    for j in range(second_start, second_end+1):
        set_two.add(j)

    set_one.intersection_update(set_two)
    if len(set_one) >= lenght:
        lenght = len(set_one)
        output = set_one

    set_one = set()
    set_two = set()
output = map(str, output)
output = ", ".join(output)
print(f"Longest intersection is [{output}] with length {lenght}")



