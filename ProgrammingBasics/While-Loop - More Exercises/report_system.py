expected_sum = int(input())
counter = 0
average_in_cash = 0
average_credit_card = 0
total_sum = 0
transaction_cash = 0
transaction_card = 0
new_sum = input()
while new_sum != "End":
    new_sum = int(new_sum)
    counter += 1
    if counter % 2 != 0:
        if new_sum > 100:
            print("Error in transaction!")
        else:
            average_in_cash += new_sum
            transaction_cash += 1
            total_sum += new_sum
            print("Product sold!")
    else:
        if new_sum < 10:
            print("Error in transaction!")
        else:
            average_credit_card += new_sum
            transaction_card += 1
            total_sum += new_sum
            print("Product sold!")

    if total_sum >= int(expected_sum):
        print(f"Average CS: {(average_in_cash / transaction_cash):.2f}")
        print(f"Average CC: {(average_credit_card / transaction_card):.2f}")
        break
    new_sum = input()
if new_sum == "End" or total_sum < int(expected_sum):
    print("Failed to collect required money for charity.")