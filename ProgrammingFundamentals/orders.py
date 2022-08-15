N = int(input())
price = 0
total_price = 0
for i in range(1, N + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price += price_per_capsule * capsules_count * days
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
    price = 0
print(f"Total: ${total_price:.2f}")

