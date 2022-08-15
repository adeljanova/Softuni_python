def math_operations(*args, **kwargs):
    output = []
    index = 0
    for el in args:
        for key, value in kwargs.items():
            if key == "a" and index == 0:
                kwargs[key] += el
            elif key == "s" and index == 1:
                kwargs[key] -= el
            elif key == "d" and index == 2:
                if el == 0.0:
                    continue
                else:
                    kwargs[key] /= el
            elif key == "m" and index == 3:
                kwargs[key] *= el
        index += 1
        if index == 4:
            index = 0

    result = {}
    for key, value in kwargs.items():
        result[key] = f"{value:.1f}"
    result = sorted(result.items(), key=lambda x: (-float(x[1]), x[0]))

    for pack in result:
        output.append(f"{pack[0]}: {pack[1]}")

    return '\n'.join(output)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
