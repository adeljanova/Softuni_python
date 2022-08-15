num_of_items = int(input())
unique_items = set()
for _ in range(num_of_items):
    compound_items = input().split()
    for item in compound_items:
        unique_items.add(item)

[print(item) for item in unique_items]
