list_of_people = input().split()
k = int(input())
counter = 0
index = 0
new_list = []
temp_list = []
for i in range(len(list_of_people)):
    temp_list.append(int(list_of_people[i]))
while len(temp_list) > 0:
    temp_person = temp_list[index]
    counter += 1
    if counter % k == 0:
        temp_list.remove(temp_person)
        new_list.append(temp_person)
    else:
        index += 1
    if index >= len(temp_list):
        index = 0
output = '[' + ','.join([str(x) for x in new_list]) + ']'
print(output)