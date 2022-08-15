num_of_logs = int(input())

counter = 0
sum = 0
temp_sum = num_of_logs
temp = []
is_zero = False

for i in range(1, num_of_logs + 1):
    for j in range(1, i + 1):
        sum += 1
        temp_sum -= 1
        if temp_sum == -1:
            is_zero = True
            break
    if is_zero:
        break
    temp.append(sum)
    sum = 0
if len(temp) == 1:
    print(len(temp))
elif temp[-1] > temp[-2]:
    for item in temp:
        counter += 1
    print(counter)
else:
    for item in temp:
        counter += 1
    print(counter - 1)

