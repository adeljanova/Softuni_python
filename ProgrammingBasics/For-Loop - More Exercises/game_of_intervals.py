num_turns = int(input())
result = 0
from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0
from_invalid = 0
for turn in range(num_turns):
    num_each_turn = int(input())
    if 0 <= num_each_turn <= 9:
        result += num_each_turn * 0.2
        from_0_9 += 1
    elif 10 <= num_each_turn <= 19:
        result += num_each_turn * 0.3
        from_10_19 += 1
    elif 20 <= num_each_turn <= 29:
        result += num_each_turn * 0.4
        from_20_29 += 1
    elif 30 <= num_each_turn <= 39:
        result += 50
        from_30_39 += 1
    elif 40 <= num_each_turn <= 50:
        result += 100
        from_40_50 += 1
    else:
        result /= 2
        from_invalid += 1
percent1 = from_0_9 / num_turns * 100
percent2 = from_10_19 / num_turns * 100
percent3 = from_20_29 / num_turns * 100
percent4 = from_30_39 / num_turns * 100
percent5 = from_40_50/ num_turns * 100
percent_invalid = from_invalid / num_turns * 100
print(f"{result:.2f}")
print(f"From 0 to 9: {percent1:.2f}%")
print(f"From 10 to 19: {percent2:.2f}%")
print(f"From 20 to 29: {percent3:.2f}%")
print(f"From 30 to 39: {percent4:.2f}%")
print(f"From 40 to 50: {percent5:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
