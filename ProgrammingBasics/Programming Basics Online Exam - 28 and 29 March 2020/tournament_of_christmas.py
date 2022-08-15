days = int(input())
total_win_counter = 0
total_lose_counter = 0
total_money_for_all = 0
for i in range(1, days + 1):
    command = input()
    win_counter = 0
    lose_counter = 0
    money = 0
    total_money = 0
    while command != "Finish":
        result = input()
        if result == "win":
            win_counter += 1
            money = 20
        elif result == "lose":
            lose_counter += 1
            money = 0
        total_money += money
        command = input()
    total_win_counter += win_counter
    total_lose_counter += lose_counter
    if win_counter > lose_counter:
        total_money += total_money * 0.1
    total_money_for_all += total_money
if total_win_counter > total_lose_counter:
    total_money_for_all += total_money_for_all * 0.2
    print(f"You won the tournament! Total raised money: {total_money_for_all:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_for_all:.2f}")
