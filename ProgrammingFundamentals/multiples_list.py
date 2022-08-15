factor = int(input())
count = int(input())
list_of_numbers = []
for index in range(1, count + 1):
    list_of_numbers.append(index * factor)
print(list_of_numbers)