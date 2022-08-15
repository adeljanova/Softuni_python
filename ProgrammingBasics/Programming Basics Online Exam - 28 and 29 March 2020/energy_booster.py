fruit = input()
size = input()
num_sets = int(input())
total = 0
if fruit == "Watermelon":
    if size == "small":
        total = num_sets * 56 * 2
    elif size == "big":
        total = num_sets * 28.70 * 5
elif fruit == "Mango":
    if size == "small":
        total = num_sets * 36.66 * 2
    elif size == "big":
        total = num_sets * 19.60 * 5
elif fruit == "Pineapple":
    if size == "small":
        total = num_sets * 42.10 * 2
    elif size == "big":
        total = num_sets * 24.80 * 5
elif fruit == "Raspberry":
    if size == "small":
        total = num_sets * 20 * 2
    elif size == "big":
        total = num_sets * 15.20 * 5
if 400 <= total <= 1000:
    total = total * 0.85
elif total > 1000:
    total = total / 2
print(f"{total:.2f} lv.")