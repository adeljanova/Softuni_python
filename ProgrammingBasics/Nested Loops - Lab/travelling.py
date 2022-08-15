collected = 0
while True:
    destination = input()
    if destination == "End":
        break
    needed_money = float(input())
    while needed_money > collected:
        saved_money = float(input())
        collected += saved_money
    if collected >= needed_money:
        print(f"Going to {destination}!")

    collected = 0




