age = float(input())
sex = input()
if sex == "m":
    if age < 16:
        print("Master")
    elif age >= 16:
        print("Mr.")
elif sex == "f":
    if age < 16:
        print("Miss")
    elif age >= 16:
        print("Ms.")