number = int(input())
dublicate = number
for i in range(1, number + 1):
    dublicate = i
    sum = 0
    while dublicate > 0:
        digit = dublicate % 10
        sum += digit
        dublicate //= 10
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> {True}")
    else:
        print(f"{i} -> {False}")

