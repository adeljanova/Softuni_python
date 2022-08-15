num_of_names = int(input())
list_of_names = []
output = []
for _ in range(num_of_names):
    name = input()
    if name not in output:
        output.append(name)
for name in output:
    print(name)