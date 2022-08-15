def data_type(command, string):
    res = ""
    if command == "int":
        res = f"{(int(string) * 2):.0f}"
    elif command == "real":
        res = f"{(float(string) * 1.5):.2f}"
    elif command == "string":
        res = f"${string}$"
    return res

declared_command = input()
declared_string = input()
print(data_type(declared_command, declared_string))