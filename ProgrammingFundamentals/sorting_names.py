string_of_names = input().split(", ")

sorted_string_of_names = sorted(string_of_names, key=lambda name: (-len(name), name))

print(sorted_string_of_names)

