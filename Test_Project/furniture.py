import re

text = input()

names = []
total_sum = 0
while text != "Purchase":
    matches = re.search(r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$", text)
    if matches:
        furniture, price, quantity = matches.groups()
        names.append(furniture)
        total_sum += (float(price) * int(quantity))
    text = input()

print("Bought furniture:")
for item in names:
    print(item)
print(f"Total money spend: {total_sum:.2f}")