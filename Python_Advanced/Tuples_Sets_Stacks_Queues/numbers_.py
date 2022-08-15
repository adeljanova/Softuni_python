first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
n = int(input())

command_list = []
numbers = ()
for j in range(n):
    data = input().split()
    if data[0] == "Add":
        if data[1] == "First":
            first_set = first_set.union([int(x) for x in data[2:]])
        elif data[1] == "Second":
            second_set = second_set.union([int(x) for x in data[2:]])
    elif data[0] == "Remove":
        if data[1] == "First":
            first_set = first_set.difference([int(x) for x in data[2:]])
        elif data[1] == "Second":
            second_set = second_set.difference([int(x) for x in data[2:]])
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")