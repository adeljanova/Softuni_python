from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = deque(map(int, input().split()))

wasted_litres = 0
while True:

    if len(cups_capacity) > 0:
        current_cup = cups_capacity[0]
    else:
        break

    if len(filled_bottles) > 0:
        current_bottle = filled_bottles.pop()
    else:
        break

    current_cup -= current_bottle
    if current_cup <= 0:
        cups_capacity.popleft()
        wasted_litres += abs(current_cup)
    else:
        while current_cup > 0:

            if len(filled_bottles) > 0:
                current_bottle = filled_bottles.pop()
            else:
                break

            current_cup -= current_bottle
        cups_capacity.popleft()
        wasted_litres += abs(current_cup)
if len(cups_capacity) == 0:
    print("Bottles:", end=" ")
    for bottle in filled_bottles:
        print(bottle, end=" ")
elif len(filled_bottles) == 0:
    print("Cups:", end=" ")
    for cup in cups_capacity:
        print(cup, end=" ")
print(f"\nWasted litters of water: {wasted_litres}")
