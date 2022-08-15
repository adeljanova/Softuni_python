concealed_message = input()
data = input()

new_message = ''
while data != "Reveal":
    split_data = data.split(":|:")
    command = split_data[0]
    if command == "InsertSpace":
        index = int(split_data[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif command == "Reverse":
        substring = split_data[1]
        if substring not in concealed_message:
            print("error")
        else:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message = concealed_message + substring
            print(concealed_message)
    elif command == "ChangeAll":
        substring = split_data[1]
        replacement = split_data[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    data = input()

print(f"You have a new text message: {concealed_message}")