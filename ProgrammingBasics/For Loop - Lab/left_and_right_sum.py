n = int(input())
sum_left = 0
sum_right = 0
for number_left in range(0, n):
    value_left = int(input())
    sum_left += value_left
for number_right in range(0, n):
    value_right = int(input())
    sum_right += value_right

difference = abs(sum_left - sum_right)
if sum_right == sum_left:
        print(f"Yes, sum = {sum_left}")
elif sum_right != sum_left:
        print(f"No, diff = {difference}")