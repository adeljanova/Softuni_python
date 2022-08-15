n = int(input())
matrix = []
sum_prime = 0
sum_secondary = 0
total_sum = 0

for i in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(n):
        if i == j:
            sum_prime += matrix[i][j]

for k in range(n):
    for s in range(n):
        if k + s == n - 1:
            sum_secondary += matrix[k][s]

total_sum = abs(sum_prime - sum_secondary)
print(total_sum)