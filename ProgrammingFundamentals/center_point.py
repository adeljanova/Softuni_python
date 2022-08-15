import math


def print_coordinates(X1, Y1, X2, Y2):
    d1 = math.sqrt(X1 * X1 + Y1 * Y1)
    d2 = math.sqrt(X2 * X2 + Y2 * Y2)
    if d1 > d2:
        abs(X2), abs(Y2)
        return f"({int(X2)}, {int(Y2)})"
    elif d1 < d2:
        abs(X1), abs(Y1)
        return f"({int(X1)}, {int(Y1)})"
    else:
        abs(X1), abs(Y1)
        return f"({int(X1)}, {int(Y1)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(print_coordinates(x1, y1, x2, y2))