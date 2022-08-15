num_rows = int(input())

destroyed_ships = 0
for row in range(1, num_rows + 1):
    rows = list(map(int, input().split()))

