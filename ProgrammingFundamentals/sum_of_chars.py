number = int(input())
sum = 0
for i in range(1, number + 1):
    symbol = input()
    sum += ord(symbol)
print(f"The sum equals: {sum}")
