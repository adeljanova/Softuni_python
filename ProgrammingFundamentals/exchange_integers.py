num_one = int(input())
num_two = int(input())
print("Before:")
print(f"a = {num_one}")
print(f"b = {num_two}")
temp = num_one
num_one = num_two
num_two = temp
print("After:")
print(f"a = {num_one}")
print(f"b = {num_two}")