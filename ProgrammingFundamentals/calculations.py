operator_as_string = input()
num_one = int(input())
num_two = int(input())

def result(operator, number1, number2):
    res = 0
    if operator == "multiply":
        res = number1 * number2
    elif operator == "divide":
        res = number1 // number2
    elif operator == "add":
        res = number1 + number2
    elif operator == "subtract":
        res = number1 - number2
    return res

print(result(operator_as_string, num_one, num_two))

