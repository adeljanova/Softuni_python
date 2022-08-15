data = input()

products = {}

while "statistics" not in data:
    command = data.split(": ")
    key = command[0]
    value = int(command[1])
    if key not in products:
        products[key] = 0
    products[key] += value
    data = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
