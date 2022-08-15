from math import sqrt


def longer_line(X1, Y1, X2, Y2, X3, Y3, X4, Y4):
    d1 = sqrt(X1 * X1 + Y1 * Y1)
    d2 = sqrt(X2 * X2 + Y2 * Y2)
    d3 = sqrt(X3 * X3 + Y3 * Y3)
    d4 = sqrt(X4 * X4 + Y4 * Y4)
    if (d1 + d2) > (d3 + d4):
        abs(X1), abs(Y1), abs(X2), abs(Y2)
        if d1 <= d2:
            return f"({int(X1)}, {int(Y1)})({int(X2)}, {int(Y2)})"
        else:
            return f"({int(X2)}, {int(Y2)})({int(X1)}, {int(Y1)})"
    else:
        abs(X3), abs(Y3), abs(X4), abs(Y4)
        if d3 <= d4:
            return f"({int(X3)}, {int(Y3)})({int(X4)}, {int(Y4)})"
        else:
            return f"({int(X4)}, {int(Y4)})({int(X3)}, {int(Y3)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))