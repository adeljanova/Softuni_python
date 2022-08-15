a = int(input())
b = int(input())
max_num_pass = int(input())
A = 35
B = 64
x = 1
y = 1
counter = 0
counterA = 1
counterB = 1
while counter != max_num_pass:
    print(chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A), "|", sep="", end="")
    counter += 1
    A += 1
    if A > 55:
        A = 35
    B += 1
    if B > 96:
        B = 64
    y += 1
    if y > b:
        x += 1
        counterA += 1
        y = 1
    counterB += 1
    if counterA == a and counterB == (b * a):
        print(chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A), "|", sep="", end="")
        break
