data = input()

for ch in range(len(data)):
    if data[ch] == ":":
        print(data[ch] + data[ch + 1])