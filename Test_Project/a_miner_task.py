data = input()

resourses = {}

data_as_list = []

while data != "stop":
    data_as_list.append(data)
    data = input()
for index in range(0, len(data_as_list), 2):
    temp = data_as_list[index]
    if temp not in resourses:
        resourses[temp] = int(data_as_list[index + 1])
    else:
        resourses[temp] += int(data_as_list[index + 1])

output = [print(f"{key} -> {value}") for key, value in resourses.items()]
