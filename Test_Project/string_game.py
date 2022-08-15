string = input()
data = input()

while data != "Done":
    split_data = data.split()
    command = split_data[0]
    if command == "Change":
        char = split_data[1]
        replacement = split_data[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        substring = split_data[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif command == "End":
        substring = split_data[1]
        if string[(len(string) - len(substring)):] == substring:
            print("True")
        else:
            print("False")
    elif command == "Uppercase":
        string = string.upper()
        print(string)
    elif command == "FindIndex":
        char = split_data[1]
        index = string.index(char)
        print(index)
    elif command == "Cut":
        startIndex = int(split_data[1])
        count = int(split_data[2])
        cut = string[startIndex:startIndex + count]
        print(cut)

    data = input()