import sys

max_number = -sys.maxsize
text = input()
while text != "Stop" :
    number = int(text)
    if number > max_number:
        max_number = number
    text = input()
print(f"{max_number}")