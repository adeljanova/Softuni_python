def sorting_cheeses(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[key] = sorted(value, key=lambda x: -x)
    result = sorted(result.items(), key=lambda x: (-len(x[1]), x[0]))
    output = []
    for item in result:
        output.append(item[0])
        output += item[1]
    return '\n'.join([str(x) for x in output])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
