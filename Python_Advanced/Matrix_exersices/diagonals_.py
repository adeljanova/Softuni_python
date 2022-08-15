n = int(input())
matrix = []
prime = []
secondary = []
sum_prime = 0
sum_secondary = 0

for i in range(n):
    matrix.append([int(x) for x in input().split(', ')])

for i in range(n):
    for j in range(n):
        if i == j:
            prime.append(matrix[i][j])
            sum_prime += matrix[i][j]

for k in range(n):
    for s in range(n):
        if k + s == n - 1:
            secondary.append(matrix[k][s])
            sum_secondary += matrix[k][s]

print(f"Primary diagonal: {', '.join([str(x) for x in prime])}. Sum: {sum_prime}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum_secondary}")
