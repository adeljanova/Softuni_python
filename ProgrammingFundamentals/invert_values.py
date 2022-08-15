list = input().split()
new_list = []
for index in range(len(list)):
    new_list.append(-int(list[index]))
print(new_list)