energy = 100
coins = 100
working_day_events = input().split("|")
isClosed = False
for event in working_day_events:
    temp_working_day_events = event.split("-")
    temp_event = temp_working_day_events[0]
    temp_energy = int(temp_working_day_events[1])
    temp_coins = int(temp_working_day_events[1])
    if "rest" in temp_working_day_events:
        if energy + temp_energy > 100:
            print("You gained 0 energy.")
        else:
            energy += temp_energy
            print(f"You gained {temp_energy} energy.")
        print(f"Current energy: {energy}.")
    elif "order" in temp_working_day_events:
        if energy - 30 >= 0:
            print(f"You earned {temp_coins} coins.")
            coins += temp_energy
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - temp_coins >= 0:
            print(f"You bought {temp_event}.")
            coins -= temp_coins
        else:
            print(f"Closed! Cannot afford {temp_event}.")
            isClosed = True
            break
if not isClosed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

