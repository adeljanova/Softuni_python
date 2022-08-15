numbers = tuple(map(float, input().split()))

counted = []
for num in numbers:
    if num not in counted:
        print(f"{num:.1f} - {numbers.count(num)} times")
    counted.append(num)