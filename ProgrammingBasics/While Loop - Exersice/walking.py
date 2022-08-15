step_counter = 0
while step_counter < 10000:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        step_counter += last_steps
        break
    more_steps = int(command)
    step_counter += more_steps
difference = abs(step_counter - 10000)
if step_counter >= 10000:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")





