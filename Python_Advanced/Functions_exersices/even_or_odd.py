def even_odd(*args):
    filter_command = args[-1]
    output = []
    if filter_command == "even":
        output = [i for i in args[:-1] if i % 2 == 0]
    else:
        output = [i for i in args[:-1] if i % 2 != 0]

    return output


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
