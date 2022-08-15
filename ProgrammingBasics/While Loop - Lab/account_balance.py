total_money = 0
while True:
    contribution = input()

    if contribution == "NoMoreMoney":
        break
    elif float(contribution) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(contribution):.2f}")
    total_money += float(contribution)

print(f"Total: {total_money:.2f}")

