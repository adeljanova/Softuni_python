def get_info(**kwargs):
    data = []
    for key, value in kwargs.items():
        data.append(kwargs[key])
    return f"This is {data[0]} from {data[1]} and he is {data[2]} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))