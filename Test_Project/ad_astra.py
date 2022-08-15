import re

text = input()
pattern = r"(?P<symbols>\#|\|)(?P<word>[ A-Za-z]{2,})(?P=symbols)(?P<date>\d{2}\/\d{2}\/\d{2})(?P=symbols)" \
          r"(?P<calories>\d{1,5})(?P=symbols)"

matches = re.findall(pattern, text)

sum = 0
for match in matches:
    sum += int(match[3])

print(f"You have food to last you for: {sum // 2000} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
