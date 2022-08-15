import re

text = input()
output = []
while True:
    if text:
        matches = re.finditer(r"www\.([\w+][-[A-Za-z0-9]+]*)\.([a-z\.]+)", text)
        for match in matches:
            output.append(match.group())
    else:
        break
    text = input()
print('\n'.join(output))