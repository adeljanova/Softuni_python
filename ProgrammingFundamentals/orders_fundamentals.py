snack = input()
quantity = int(input())

def result(snack_of_choice, quantity_of_choice):
    res = 0
    if snack_of_choice == "coffee":
        res = quantity_of_choice * 1.50
    elif snack_of_choice == "water":
        res = quantity_of_choice * 1.00
    elif snack_of_choice == "coke":
        res = quantity_of_choice * 1.40
    elif snack_of_choice == "snacks":
        res = quantity_of_choice * 2.00
    return f"{res:.2f}"

print(result(snack, quantity))
