import sys

min_number = sys.maxsize
text = input()
while text != "Stop":
    number = int(text)
    if number < min_number:
        min_number = number
    text = input()
print(f"{min_number}")