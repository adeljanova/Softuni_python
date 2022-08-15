from collections import deque

quantity_of_food = int(input())
quantity = input().split()
quantity_of_order = deque(quantity)

max_num = 0
for num in quantity:
    num = int(num)
    if int(num) > max_num:
        max_num = num
print(max_num)

while quantity_of_order:
    current_order = int(quantity_of_order[0])
    if current_order <= quantity_of_food:
        quantity_of_food -= current_order
        quantity_of_order.popleft()
    else:
        break

if quantity_of_order:
    print(f"Orders left: {' '.join(quantity_of_order)}")
else:
    print("Orders complete")