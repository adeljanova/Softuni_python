n = int(input())
sum_even = 0
sum_odd = 0
for number_even in range(0, n):
    value = int(input())
    if number_even % 2 == 0:
        sum_even += value
    else:
        sum_odd += value
difference = abs(sum_even - sum_odd)
if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    print("No")
    print(f"Diff = {difference}")