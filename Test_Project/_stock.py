info = input().split(" ")
bakery = dict()

for i in range(0, len(info), 2):
    key = info[i]
    value = info[i + 1]
    bakery[key] = int(value)

check = input().split(" ")
for item in check:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
