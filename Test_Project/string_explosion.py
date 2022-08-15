data = input()

strength = 0
new_text = ''
for index in range(len(data)):
    if data[index] != ">" and strength > 0:
        strength -= 1
    elif data[index] == ">":
        strength += int(data[index + 1])
        new_text += data[index]
    else:
        new_text += data[index]
print(new_text)