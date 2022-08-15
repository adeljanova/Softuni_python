number = int(input())
current = 1
current_bigger = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        if current > number:
            current_bigger = True
            break
        print(str(current) + " ", end="")
        current += 1
    if current_bigger:
        break
    print()