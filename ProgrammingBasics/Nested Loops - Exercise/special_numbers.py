number = int(input())

for n in range(1111, 10000):
    special_number = True
    n_as_str = str(n)
    for digit in n_as_str:
        if int(digit) == 0 or number % int(digit) != 0:
            special_number = False
            break
    if special_number:
        print(n, end=" ")




