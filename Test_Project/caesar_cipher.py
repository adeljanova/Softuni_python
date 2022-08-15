data = input()
encrypted_message = ''
for ch in data:
    temp = ord(ch) + 3
    encrypted_message += chr(temp)

print(encrypted_message)