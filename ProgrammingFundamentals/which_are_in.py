samples = input().split(", ")
list_of_strings = input()

new_list = [sample for sample in samples if sample in list_of_strings]

print(new_list)

