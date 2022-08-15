import re

text = input()
output = re.findall(r"\b[A-Z][a-z]+ \b[A-Z][a-z]+\b", text)
print(" ".join(output))