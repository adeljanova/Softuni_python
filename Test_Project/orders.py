list_of_items = input()

products = {}
price_list = {}

total = 0

while list_of_items != "buy":
    name, price, quantity = list_of_items.split()
    if name not in products:
        products[name] = int(quantity)
        price_list[name] = float(price)
    else:
        products[name] += int(quantity)
        if price_list[name] != price:
            price_list[name] = price

    list_of_items = input()

for (key, value), (key2, value2) in zip(products.items(), price_list.items()):
    total = value * float(value2)
    print(f"{key} -> {total:.2f}")


