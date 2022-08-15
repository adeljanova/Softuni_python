number = int(input())
flag = True
if number == 0 or number == 1:
    print("False")
for i in range(2, (number // 2) + 1):
    if number % i == 0:
        flag = False
        break
if flag:
    print("True")
else:
    print("False")
