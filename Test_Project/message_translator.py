import re
n = int(input())

pattern = r"(?P<symbol>!)(?P<command>[A-Z][a-z]{3,})(?P=symbol):(?P<bracket1>\[)" \
          r"(?P<string>[A-Za-z]{8,})(?P<bracket2>\])"
command = r"(?P<symbol>!)(?P<command>[A-Z][a-z]{3,})(?P=symbol)"
string = r"(?P<bracket1>\[)(?P<string>[A-Za-z]{8,})(?P<bracket2>\])"
for i in range(n):
    text = input()
    matches = re.findall(pattern, text)
    if not matches:
        print("\nThe message is invalid")
    else:
        com = re.findall(command, text)
        str = re.findall(string, text)
        print(f"{com[0][1]}:", end=" ")
        for char in str[0][1]:
            print(ord(char), end=" ")
