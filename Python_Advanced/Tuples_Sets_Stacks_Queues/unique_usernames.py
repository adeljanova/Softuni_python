num_of_names = int(input())
unique_names = set()

for _ in range(num_of_names):
    name = input()
    unique_names.add(name)

[print(name) for name in unique_names]