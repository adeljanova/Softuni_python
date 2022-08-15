import json.decoder
import re

text = input()
matches = re.finditer(r"(?<=\s)([a-z0-9]+[\.\_\-a-z0-9]+)@([a-z0-9]+[-a-z0-9]*)\.([\.a-z]+)\b", text)
output = []
for match in matches:
    output.append(match.group())

print('\n'.join(output))