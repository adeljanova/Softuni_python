key = int(input())
num_of_lines = int(input())
message = ""
for i in range(1, num_of_lines + 1):
    lower_case = input()
    upper_case = input()
    value_lower = ord(lower_case) + key
    value_upper = ord(upper_case) + key
    message += chr(value_lower) + chr(value_upper)
print(message)
