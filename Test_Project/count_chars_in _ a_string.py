string = input().split()

counter_dict = {}

for word in string:
    for ch in word:
        if ch not in counter_dict:
            counter_dict[ch] = 1
        else:
            counter_dict[ch] += 1

output = [print(f"{key} -> {value}") for key, value in counter_dict.items()]
