i = 1
while i >= 0:
    i = float(input())
    if i >= 0:
        i = i * 2
        print(f"Result: {i:.2f}")
    else:
        print(f"Negative number!")
