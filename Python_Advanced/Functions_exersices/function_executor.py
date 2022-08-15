def func_executor(*args):
    result = []
    for function_reference, function_parameters in args:
        func_res = function_reference(*function_parameters)
        result.append(f"{function_reference.__name__} - {func_res}")

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
