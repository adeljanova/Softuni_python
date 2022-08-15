def operate(operation, *args):
    result = args[0]
    for el in args[1:]:
        if operation == "+":
            result += el
        elif operation == "-":
            result -= el
        elif operation == "*":
            result *= el
        elif operation == "/":
            result /= el

    return result


print(operate("/", 0, 2, 3))
print(operate("*", 3, 4))
