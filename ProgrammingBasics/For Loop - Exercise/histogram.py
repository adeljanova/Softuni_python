n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for number in range(n):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    else:
        p5 += 1
print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
print(f"{p4 / n * 100:.2f}%")
print(f"{p5 / n * 100:.2f}%")