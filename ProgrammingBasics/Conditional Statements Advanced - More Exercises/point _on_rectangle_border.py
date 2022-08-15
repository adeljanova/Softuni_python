x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = float(input())
y = float(input())
first_condition = True
second_condition = True
if first_condition == (x == x1 or x == x2) and (y1 < y <= y2):
    first_condition = True
else:
    first_condition = False
if second_condition == (y == y1 or y == y2) and (x1 < x <= x2):
    second_condition = True
else:
    second_condition = False
if first_condition or second_condition:
    print("Border")
else:
    print("Inside / Outside")