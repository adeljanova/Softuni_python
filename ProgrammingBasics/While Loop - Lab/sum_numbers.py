number = int(input())
sum = 0
while sum < number:
    new_number = int(input())
    sum += new_number
    if sum > number:
        break
print(sum)
