import re

text = input()

output = []
while True:
    if text:
        matches = re.finditer(r"\d+", text)
        for match in matches:
            output.append(match.group())
    else:
        break
    text = input()
print(" ".join(output))
