divisor = int(input())
boundary = int(input())
N = 0
for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i <= boundary:
            if i > 0:
                N = i
print(N)